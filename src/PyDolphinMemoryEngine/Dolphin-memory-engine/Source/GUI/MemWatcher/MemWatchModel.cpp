#include "MemWatchModel.h"

#include <QDataStream>
#include <QMimeData>
#include <cstring>
#include <sstream>

#include "../GUICommon.h"

MemWatchModel::MemWatchModel(QObject* parent) : QAbstractItemModel(parent)
{
  m_rootNode = new MemWatchTreeNode(nullptr);
}

MemWatchModel::~MemWatchModel()
{
  delete m_rootNode;
}

void MemWatchModel::onUpdateTimer()
{
  if (!updateNodeValueRecursive(m_rootNode))
  {
    emit readFailed();
  }
}

void MemWatchModel::onFreezeTimer()
{
  if (!freezeNodeValueRecursive(m_rootNode))
  {
    emit writeFailed(QModelIndex(), Common::MemOperationReturnCode::operationFailed);
  }
}

bool MemWatchModel::updateNodeValueRecursive(MemWatchTreeNode* node, const QModelIndex& parent,
                                             bool readSucess)
{
  QVector<MemWatchTreeNode*> children = node->getChildren();
  if (children.count() != 0)
  {
    for (auto i : children)
    {
      QModelIndex theIndex = index(i->getRow(), WATCH_COL_VALUE, parent);
      readSucess = updateNodeValueRecursive(i, theIndex, readSucess);
      if (!readSucess)
        return false;
      if (!GUICommon::g_valueEditing)
        emit dataChanged(theIndex, theIndex);
    }
  }

  MemWatchEntry* entry = node->getEntry();
  if (entry != nullptr)
    if (entry->readMemoryFromRAM() == Common::MemOperationReturnCode::operationFailed)
      return false;
  return true;
}

bool MemWatchModel::freezeNodeValueRecursive(MemWatchTreeNode* node, const QModelIndex& parent,
                                             bool writeSucess)
{
  QVector<MemWatchTreeNode*> children = node->getChildren();
  if (children.count() != 0)
  {
    for (auto i : children)
    {
      QModelIndex theIndex = index(i->getRow(), WATCH_COL_VALUE, parent);
      writeSucess = freezeNodeValueRecursive(i, theIndex, writeSucess);
      if (!writeSucess)
        return false;
    }
  }

  MemWatchEntry* entry = node->getEntry();
  if (entry != nullptr)
  {
    if (entry->isLocked())
    {
      Common::MemOperationReturnCode writeReturn = entry->freeze();
      // Here we want to not care about invalid pointers, it won't write anyway
      if (writeReturn == Common::MemOperationReturnCode::OK ||
          writeReturn == Common::MemOperationReturnCode::invalidPointer)
        return true;
    }
  }
  return true;
}

void MemWatchModel::changeType(const QModelIndex& index, Common::MemType type, size_t length)
{
  MemWatchEntry* entry = getEntryFromIndex(index);
  entry->setType(type);
  entry->setLength(length);
  emit dataChanged(index, index);
}

MemWatchEntry* MemWatchModel::getEntryFromIndex(const QModelIndex& index) const
{
  MemWatchTreeNode* node = static_cast<MemWatchTreeNode*>(index.internalPointer());
  return node->getEntry();
}

void MemWatchModel::addGroup(const QString& name)
{
  const QModelIndex rootIndex = index(0, 0);
  MemWatchTreeNode* node = new MemWatchTreeNode(nullptr, m_rootNode, true, name);
  beginInsertRows(rootIndex, rowCount(rootIndex), rowCount(rootIndex));
  m_rootNode->appendChild(node);
  endInsertRows();
  emit layoutChanged();
}

void MemWatchModel::addEntry(MemWatchEntry* entry)
{
  MemWatchTreeNode* newNode = new MemWatchTreeNode(entry);
  QModelIndex idx = index(0, 0);
  beginInsertRows(idx, rowCount(QModelIndex()), rowCount(QModelIndex()));
  m_rootNode->appendChild(newNode);
  endInsertRows();
  emit layoutChanged();
}

void MemWatchModel::editEntry(MemWatchEntry* entry, const QModelIndex& index)
{
  MemWatchTreeNode* node = static_cast<MemWatchTreeNode*>(index.internalPointer());
  node->setEntry(entry);
  emit layoutChanged();
}

void MemWatchModel::removeNode(const QModelIndex& index)
{
  if (index.isValid())
  {
    MemWatchTreeNode* toDelete = static_cast<MemWatchTreeNode*>(index.internalPointer());
    MemWatchTreeNode* parent = toDelete->getParent();

    int toDeleteRow = toDelete->getRow();

    const QModelIndex idx = createIndex(toDeleteRow, 0, parent);
    if (parent == m_rootNode)
      beginRemoveRows(QModelIndex(), toDeleteRow, toDeleteRow);
    else
      beginRemoveRows(idx.parent(), toDeleteRow, toDeleteRow);
    bool removeChildren = (toDelete->isGroup() && toDelete->hasChildren());
    if (removeChildren)
      beginRemoveRows(index, 0, toDelete->childrenCount());
    toDelete->getParent()->removeChild(toDeleteRow);
    delete toDelete;
    if (removeChildren)
      endRemoveRows();
    endRemoveRows();
  }
}

int MemWatchModel::columnCount(const QModelIndex& parent) const
{
  return WATCH_COL_NUM;
}

int MemWatchModel::rowCount(const QModelIndex& parent) const
{
  MemWatchTreeNode* parentItem;
  if (parent.column() > 0)
    return 0;

  if (!parent.isValid())
    parentItem = m_rootNode;
  else
    parentItem = static_cast<MemWatchTreeNode*>(parent.internalPointer());

  return parentItem->getChildren().size();
}

QVariant MemWatchModel::data(const QModelIndex& index, int role) const
{
  if (!index.isValid())
    return QVariant();

  MemWatchTreeNode* item = static_cast<MemWatchTreeNode*>(index.internalPointer());

  if (!item->isGroup())
  {
    if (role == Qt::EditRole && index.column() == WATCH_COL_TYPE)
    {
      return QVariant(static_cast<int>(item->getEntry()->getType()));
    }

    MemWatchEntry* entry = item->getEntry();
    if (role == Qt::DisplayRole || role == Qt::EditRole)
    {
      switch (index.column())
      {
      case WATCH_COL_LABEL:
      {
        return QString::fromStdString(entry->getLabel());
        break;
      }
      case WATCH_COL_TYPE:
      {
        Common::MemType type = entry->getType();
        size_t length = entry->getLength();
        return GUICommon::getStringFromType(type, length);
        break;
      }
      case WATCH_COL_ADDRESS:
      {
        u32 address = entry->getConsoleAddress();
        bool isPointer = entry->isBoundToPointer();
        return getAddressString(address, isPointer);
        break;
      }
      case WATCH_COL_VALUE:
      {
        return QString::fromStdString(entry->getStringFromMemory());
        break;
      }
      }
    }
    else if (role == Qt::CheckStateRole && index.column() == WATCH_COL_LOCK)
    {
      if (entry->isLocked())
        return Qt::Checked;
      return Qt::Unchecked;
    }
  }
  else
  {
    if (index.column() == 0 && role == Qt::DisplayRole)
      return item->getGroupName();
  }
  return QVariant();
}

bool MemWatchModel::setData(const QModelIndex& index, const QVariant& value, int role)
{
  if (!index.isValid())
    return false;

  MemWatchTreeNode* node = static_cast<MemWatchTreeNode*>(index.internalPointer());
  if (node == m_rootNode)
    return false;

  if (!node->isGroup())
  {
    MemWatchEntry* entry = node->getEntry();
    if (role == Qt::EditRole)
    {
      switch (index.column())
      {
      case WATCH_COL_LABEL:
      {
        entry->setLabel((value.toString().toStdString()));
        emit dataChanged(index, index);
        return true;
        break;
      }
      case WATCH_COL_VALUE:
      {
        Common::MemOperationReturnCode returnCode =
            entry->writeMemoryFromString((value.toString().toStdString()));
        if (returnCode != Common::MemOperationReturnCode::OK)
        {
          emit writeFailed(index, returnCode);
          return false;
        }
        emit dataChanged(index, index);
        return true;
        break;
      }
      default:
        return false;
      }
    }
    else if (role == Qt::CheckStateRole && index.column() == WATCH_COL_LOCK)
    {
      value == Qt::Checked ? entry->setLock(true) : entry->setLock(false);
      emit dataChanged(index, index);
      return true;
    }
    else
    {
      return false;
    }
  }
  else
  {
    node->setGroupName(value.toString());
    return true;
  }
}

Qt::ItemFlags MemWatchModel::flags(const QModelIndex& index) const
{
  if (!index.isValid())
    return Qt::ItemIsDropEnabled;

  MemWatchTreeNode* node = static_cast<MemWatchTreeNode*>(index.internalPointer());
  if (node == m_rootNode)
    return Qt::ItemIsEditable | Qt::ItemIsEnabled | Qt::ItemIsSelectable;

  // These flags are common to every node
  Qt::ItemFlags flags = Qt::ItemIsSelectable | Qt::ItemIsDragEnabled | Qt::ItemIsEnabled;

  if (node->isGroup())
  {
    flags |= Qt::ItemIsDropEnabled;
    if (index.column() == WATCH_COL_LABEL)
      flags |= Qt::ItemIsEditable;
    return flags;
  }

  if (index.column() == WATCH_COL_LOCK)
    return flags |= Qt::ItemIsUserCheckable;

  if (index.column() != WATCH_COL_ADDRESS && index.column() != WATCH_COL_TYPE)
    flags |= Qt::ItemIsEditable;
  return flags;
}

QModelIndex MemWatchModel::index(int row, int column, const QModelIndex& parent) const
{
  if (!hasIndex(row, column, parent))
    return QModelIndex();

  MemWatchTreeNode* parentNode;

  if (!parent.isValid())
    parentNode = m_rootNode;
  else
    parentNode = static_cast<MemWatchTreeNode*>(parent.internalPointer());

  MemWatchTreeNode* childNode = parentNode->getChildren().at(row);
  if (childNode)
    return createIndex(row, column, childNode);
  else
    return QModelIndex();
}

QModelIndex MemWatchModel::parent(const QModelIndex& index) const
{
  if (!index.isValid())
    return QModelIndex();

  MemWatchTreeNode* childNode = static_cast<MemWatchTreeNode*>(index.internalPointer());
  MemWatchTreeNode* parentNode = childNode->getParent();

  if (parentNode == m_rootNode)
    return QModelIndex();

  return createIndex(parentNode->getRow(), 0, parentNode);
}

QVariant MemWatchModel::headerData(int section, Qt::Orientation orientation, int role) const
{
  if (orientation == Qt::Horizontal && role == Qt::DisplayRole)
  {
    switch (section)
    {
    case WATCH_COL_LABEL:
      return QString("Name");
      break;
    case WATCH_COL_TYPE:
      return QString("Type");
      break;
    case WATCH_COL_ADDRESS:
      return QString("Address");
      break;
    case WATCH_COL_VALUE:
      return QString("Value");
      break;
    case WATCH_COL_LOCK:
      return QString("Lock");
      break;
    }
  }
  return QVariant();
}

Qt::DropActions MemWatchModel::supportedDropActions() const
{
  return Qt::MoveAction;
}

Qt::DropActions MemWatchModel::supportedDragActions() const
{
  return Qt::MoveAction;
}

QStringList MemWatchModel::mimeTypes() const
{
  return QStringList() << "application/x-memwatchtreenode";
}

QMimeData* MemWatchModel::mimeData(const QModelIndexList& indexes) const
{
  QMimeData* mimeData = new QMimeData;
  QByteArray data;

  QDataStream stream(&data, QIODevice::WriteOnly);
  QList<MemWatchTreeNode*> nodes;

  foreach (const QModelIndex& index, indexes)
  {
    MemWatchTreeNode* node = static_cast<MemWatchTreeNode*>(index.internalPointer());
    if (!nodes.contains(node))
      nodes << node;
  }
  stream << nodes.count();
  foreach (MemWatchTreeNode* node, nodes)
  {
    qulonglong pointer = 0;
    std::memcpy(&pointer, &node, sizeof(node));
    stream << pointer;
  }
  mimeData->setData("application/x-memwatchtreenode", data);
  return mimeData;
}

bool MemWatchModel::dropMimeData(const QMimeData* data, Qt::DropAction action, int row, int column,
                                 const QModelIndex& parent)
{
  if (!data->hasFormat("application/x-memwatchtreenode"))
  {
    return false;
  }
  QByteArray bytes = data->data("application/x-memwatchtreenode");
  QDataStream stream(&bytes, QIODevice::ReadOnly);
  MemWatchTreeNode* destParentNode = nullptr;
  if (!parent.isValid())
    destParentNode = m_rootNode;
  else
    destParentNode = static_cast<MemWatchTreeNode*>(parent.internalPointer());
  int count;
  stream >> count;
  if (row == -1)
  {
    if (parent.isValid() && destParentNode->isGroup())
      row = rowCount(parent);
    else if (!parent.isValid())
      return false;
  }
  for (int i = 0; i < count; ++i)
  {
    qlonglong nodePtr;
    stream >> nodePtr;
    MemWatchTreeNode* srcNode = nullptr;
    std::memcpy(&srcNode, &nodePtr, sizeof(nodePtr));

    if (srcNode->getRow() < row && destParentNode == srcNode->getParent())
      --row;

    const int srcNodeRow = srcNode->getRow();

    const QModelIndex idx = createIndex(srcNodeRow, 0, destParentNode);
    if (destParentNode == m_rootNode)
      beginRemoveRows(QModelIndex(), srcNodeRow, srcNodeRow);
    else
      beginRemoveRows(idx.parent(), srcNodeRow, srcNodeRow);
    srcNode->getParent()->removeChild(srcNodeRow);
    endRemoveRows();

    beginInsertRows(parent, row, row);
    destParentNode->insertChild(row, srcNode);
    endInsertRows();

    ++row;
  }
  emit dropSucceeded();
  return true;
}

QString MemWatchModel::getAddressString(u32 address, bool isPointer) const
{
  std::stringstream ss;
  if (isPointer)
  {
    ss << "P->" << std::hex << std::uppercase << address;
    return QString::fromStdString(ss.str());
  }
  ss << std::hex << std::uppercase << address;
  return QString::fromStdString(ss.str());
}

void MemWatchModel::loadRootFromJsonRecursive(const QJsonObject& json)
{
  m_rootNode->readFromJson(json);
  emit layoutChanged();
}

void MemWatchModel::writeRootToJsonRecursive(QJsonObject& json) const
{
  m_rootNode->writeToJson(json);
}

QString MemWatchModel::writeRootToCSVStringRecursive() const
{
  QString csv = QString("Name;Address[offsets] (in hex);Type\n");
  csv.append(m_rootNode->writeAsCSV());
  if (csv.endsWith("\n"))
    csv.remove(csv.length() - 1, 1);
  return csv;
}

bool MemWatchModel::hasAnyNodes() const
{
  return m_rootNode->hasChildren();
}

MemWatchTreeNode* MemWatchModel::getTreeNodeFromIndex(const QModelIndex& index) const
{
  return static_cast<MemWatchTreeNode*>(index.internalPointer());
}