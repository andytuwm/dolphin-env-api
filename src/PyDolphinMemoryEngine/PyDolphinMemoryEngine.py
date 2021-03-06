# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_PyDolphinMemoryEngine')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_PyDolphinMemoryEngine')
    _PyDolphinMemoryEngine = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_PyDolphinMemoryEngine', [dirname(__file__)])
        except ImportError:
            import _PyDolphinMemoryEngine
            return _PyDolphinMemoryEngine
        if fp is not None:
            try:
                _mod = imp.load_module('_PyDolphinMemoryEngine', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _PyDolphinMemoryEngine = swig_import_helper()
    del swig_import_helper
else:
    import _PyDolphinMemoryEngine
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class MemWatchEntry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MemWatchEntry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MemWatchEntry, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _PyDolphinMemoryEngine.new_MemWatchEntry(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyDolphinMemoryEngine.delete_MemWatchEntry
    __del__ = lambda self: None

    def getLabel(self) -> "std::string":
        return _PyDolphinMemoryEngine.MemWatchEntry_getLabel(self)

    def getType(self) -> "Common::MemType":
        return _PyDolphinMemoryEngine.MemWatchEntry_getType(self)

    def getConsoleAddress(self) -> "u32":
        return _PyDolphinMemoryEngine.MemWatchEntry_getConsoleAddress(self)

    def isLocked(self) -> "bool":
        return _PyDolphinMemoryEngine.MemWatchEntry_isLocked(self)

    def isBoundToPointer(self) -> "bool":
        return _PyDolphinMemoryEngine.MemWatchEntry_isBoundToPointer(self)

    def getBase(self) -> "Common::MemBase":
        return _PyDolphinMemoryEngine.MemWatchEntry_getBase(self)

    def getLength(self) -> "size_t":
        return _PyDolphinMemoryEngine.MemWatchEntry_getLength(self)

    def getMemory(self) -> "char *":
        return _PyDolphinMemoryEngine.MemWatchEntry_getMemory(self)

    def isUnsigned(self) -> "bool":
        return _PyDolphinMemoryEngine.MemWatchEntry_isUnsigned(self)

    def getPointerOffset(self, index: 'int const') -> "int":
        return _PyDolphinMemoryEngine.MemWatchEntry_getPointerOffset(self, index)

    def getPointerOffsets(self) -> "std::vector< int >":
        return _PyDolphinMemoryEngine.MemWatchEntry_getPointerOffsets(self)

    def getPointerLevel(self) -> "size_t":
        return _PyDolphinMemoryEngine.MemWatchEntry_getPointerLevel(self)

    def setLabel(self, label: 'std::string const &') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setLabel(self, label)

    def setConsoleAddress(self, address: 'u32 const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setConsoleAddress(self, address)

    def setType(self, type: 'Common::MemType const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setType(self, type)

    def setBase(self, base: 'Common::MemBase const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setBase(self, base)

    def setLock(self, doLock: 'bool const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setLock(self, doLock)

    def setLength(self, length: 'size_t const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setLength(self, length)

    def setSignedUnsigned(self, isUnsigned: 'bool const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setSignedUnsigned(self, isUnsigned)

    def setBoundToPointer(self, boundToPointer: 'bool const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setBoundToPointer(self, boundToPointer)

    def setPointerOffset(self, pointerOffset: 'int const', index: 'int const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_setPointerOffset(self, pointerOffset, index)

    def addOffset(self, offset: 'int const') -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_addOffset(self, offset)

    def removeOffset(self) -> "void":
        return _PyDolphinMemoryEngine.MemWatchEntry_removeOffset(self)

    def freeze(self) -> "Common::MemOperationReturnCode":
        return _PyDolphinMemoryEngine.MemWatchEntry_freeze(self)

    def getAddressForPointerLevel(self, level: 'int const') -> "u32":
        return _PyDolphinMemoryEngine.MemWatchEntry_getAddressForPointerLevel(self, level)

    def getAddressStringForPointerLevel(self, level: 'int const') -> "std::string":
        return _PyDolphinMemoryEngine.MemWatchEntry_getAddressStringForPointerLevel(self, level)

    def readMemoryFromRAM(self) -> "Common::MemOperationReturnCode":
        return _PyDolphinMemoryEngine.MemWatchEntry_readMemoryFromRAM(self)

    def getStringFromMemory(self) -> "std::string":
        return _PyDolphinMemoryEngine.MemWatchEntry_getStringFromMemory(self)

    def writeMemoryFromString(self, inputString: 'std::string const &') -> "Common::MemOperationReturnCode":
        return _PyDolphinMemoryEngine.MemWatchEntry_writeMemoryFromString(self, inputString)
MemWatchEntry_swigregister = _PyDolphinMemoryEngine.MemWatchEntry_swigregister
MemWatchEntry_swigregister(MemWatchEntry)

class MemScanner(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MemScanner, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MemScanner, name)
    __repr__ = _swig_repr
    ScanFiter_exact = _PyDolphinMemoryEngine.MemScanner_ScanFiter_exact
    ScanFiter_increasedBy = _PyDolphinMemoryEngine.MemScanner_ScanFiter_increasedBy
    ScanFiter_decreasedBy = _PyDolphinMemoryEngine.MemScanner_ScanFiter_decreasedBy
    ScanFiter_between = _PyDolphinMemoryEngine.MemScanner_ScanFiter_between
    ScanFiter_biggerThan = _PyDolphinMemoryEngine.MemScanner_ScanFiter_biggerThan
    ScanFiter_smallerThan = _PyDolphinMemoryEngine.MemScanner_ScanFiter_smallerThan
    ScanFiter_increased = _PyDolphinMemoryEngine.MemScanner_ScanFiter_increased
    ScanFiter_decreased = _PyDolphinMemoryEngine.MemScanner_ScanFiter_decreased
    ScanFiter_changed = _PyDolphinMemoryEngine.MemScanner_ScanFiter_changed
    ScanFiter_unchanged = _PyDolphinMemoryEngine.MemScanner_ScanFiter_unchanged
    ScanFiter_unknownInitial = _PyDolphinMemoryEngine.MemScanner_ScanFiter_unknownInitial
    CompareResult_bigger = _PyDolphinMemoryEngine.MemScanner_CompareResult_bigger
    CompareResult_smaller = _PyDolphinMemoryEngine.MemScanner_CompareResult_smaller
    CompareResult_equal = _PyDolphinMemoryEngine.MemScanner_CompareResult_equal
    CompareResult_nan = _PyDolphinMemoryEngine.MemScanner_CompareResult_nan

    def __init__(self):
        this = _PyDolphinMemoryEngine.new_MemScanner()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyDolphinMemoryEngine.delete_MemScanner
    __del__ = lambda self: None

    def firstScan(self, filter: 'MemScanner::ScanFiter const', searchTerm1: 'std::string const &', searchTerm2: 'std::string const &') -> "Common::MemOperationReturnCode":
        return _PyDolphinMemoryEngine.MemScanner_firstScan(self, filter, searchTerm1, searchTerm2)

    def nextScan(self, filter: 'MemScanner::ScanFiter const', searchTerm1: 'std::string const &', searchTerm2: 'std::string const &') -> "Common::MemOperationReturnCode":
        return _PyDolphinMemoryEngine.MemScanner_nextScan(self, filter, searchTerm1, searchTerm2)

    def reset(self) -> "void":
        return _PyDolphinMemoryEngine.MemScanner_reset(self)

    def compareMemoryAsNumbers(self, first: 'char const *', second: 'char const *', offset: 'char const *', offsetInvert: 'bool', bswapSecond: 'bool', length: 'size_t') -> "MemScanner::CompareResult":
        return _PyDolphinMemoryEngine.MemScanner_compareMemoryAsNumbers(self, first, second, offset, offsetInvert, bswapSecond, length)

    def setType(self, type: 'Common::MemType const') -> "void":
        return _PyDolphinMemoryEngine.MemScanner_setType(self, type)

    def setBase(self, base: 'Common::MemBase const') -> "void":
        return _PyDolphinMemoryEngine.MemScanner_setBase(self, base)

    def setIsSigned(self, isSigned: 'bool const') -> "void":
        return _PyDolphinMemoryEngine.MemScanner_setIsSigned(self, isSigned)

    def getResultsConsoleAddr(self) -> "std::vector< u32 >":
        return _PyDolphinMemoryEngine.MemScanner_getResultsConsoleAddr(self)

    def getResultCount(self) -> "size_t":
        return _PyDolphinMemoryEngine.MemScanner_getResultCount(self)

    def getTermsNumForFilter(self, filter: 'MemScanner::ScanFiter const') -> "int":
        return _PyDolphinMemoryEngine.MemScanner_getTermsNumForFilter(self, filter)

    def getType(self) -> "Common::MemType":
        return _PyDolphinMemoryEngine.MemScanner_getType(self)

    def getBase(self) -> "Common::MemBase":
        return _PyDolphinMemoryEngine.MemScanner_getBase(self)

    def getLength(self) -> "size_t":
        return _PyDolphinMemoryEngine.MemScanner_getLength(self)

    def getIsUnsigned(self) -> "bool":
        return _PyDolphinMemoryEngine.MemScanner_getIsUnsigned(self)

    def getFormattedScannedValueAt(self, index: 'int const') -> "std::string":
        return _PyDolphinMemoryEngine.MemScanner_getFormattedScannedValueAt(self, index)

    def updateCurrentRAMCache(self) -> "Common::MemOperationReturnCode":
        return _PyDolphinMemoryEngine.MemScanner_updateCurrentRAMCache(self)

    def getFormattedCurrentValueAt(self, index: 'int') -> "std::string":
        return _PyDolphinMemoryEngine.MemScanner_getFormattedCurrentValueAt(self, index)

    def typeSupportsAdditionalOptions(self, type: 'Common::MemType const') -> "bool":
        return _PyDolphinMemoryEngine.MemScanner_typeSupportsAdditionalOptions(self, type)

    def hasScanStarted(self) -> "bool":
        return _PyDolphinMemoryEngine.MemScanner_hasScanStarted(self)
MemScanner_swigregister = _PyDolphinMemoryEngine.MemScanner_swigregister
MemScanner_swigregister(MemScanner)

class DolphinAccessor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DolphinAccessor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DolphinAccessor, name)
    __repr__ = _swig_repr
    DolphinStatus_hooked = _PyDolphinMemoryEngine.DolphinAccessor_DolphinStatus_hooked
    DolphinStatus_notRunning = _PyDolphinMemoryEngine.DolphinAccessor_DolphinStatus_notRunning
    DolphinStatus_noEmu = _PyDolphinMemoryEngine.DolphinAccessor_DolphinStatus_noEmu
    DolphinStatus_unHooked = _PyDolphinMemoryEngine.DolphinAccessor_DolphinStatus_unHooked
    if _newclass:
        init = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_init)
    else:
        init = _PyDolphinMemoryEngine.DolphinAccessor_init
    if _newclass:
        hook = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_hook)
    else:
        hook = _PyDolphinMemoryEngine.DolphinAccessor_hook
    if _newclass:
        unHook = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_unHook)
    else:
        unHook = _PyDolphinMemoryEngine.DolphinAccessor_unHook
    if _newclass:
        readFromRAM = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_readFromRAM)
    else:
        readFromRAM = _PyDolphinMemoryEngine.DolphinAccessor_readFromRAM
    if _newclass:
        writeToRAM = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_writeToRAM)
    else:
        writeToRAM = _PyDolphinMemoryEngine.DolphinAccessor_writeToRAM
    if _newclass:
        getPID = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_getPID)
    else:
        getPID = _PyDolphinMemoryEngine.DolphinAccessor_getPID
    if _newclass:
        getEmuRAMAddressStart = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_getEmuRAMAddressStart)
    else:
        getEmuRAMAddressStart = _PyDolphinMemoryEngine.DolphinAccessor_getEmuRAMAddressStart
    if _newclass:
        getStatus = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_getStatus)
    else:
        getStatus = _PyDolphinMemoryEngine.DolphinAccessor_getStatus
    if _newclass:
        enableMem2 = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_enableMem2)
    else:
        enableMem2 = _PyDolphinMemoryEngine.DolphinAccessor_enableMem2
    if _newclass:
        isMem2Enabled = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_isMem2Enabled)
    else:
        isMem2Enabled = _PyDolphinMemoryEngine.DolphinAccessor_isMem2Enabled
    if _newclass:
        autoDetectMem2 = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_autoDetectMem2)
    else:
        autoDetectMem2 = _PyDolphinMemoryEngine.DolphinAccessor_autoDetectMem2
    if _newclass:
        updateRAMCache = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_updateRAMCache)
    else:
        updateRAMCache = _PyDolphinMemoryEngine.DolphinAccessor_updateRAMCache
    if _newclass:
        getFormattedValueFromCache = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_getFormattedValueFromCache)
    else:
        getFormattedValueFromCache = _PyDolphinMemoryEngine.DolphinAccessor_getFormattedValueFromCache
    if _newclass:
        copyRawMemoryFromCache = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_copyRawMemoryFromCache)
    else:
        copyRawMemoryFromCache = _PyDolphinMemoryEngine.DolphinAccessor_copyRawMemoryFromCache
    if _newclass:
        isValidConsoleAddress = staticmethod(_PyDolphinMemoryEngine.DolphinAccessor_isValidConsoleAddress)
    else:
        isValidConsoleAddress = _PyDolphinMemoryEngine.DolphinAccessor_isValidConsoleAddress

    def __init__(self):
        this = _PyDolphinMemoryEngine.new_DolphinAccessor()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyDolphinMemoryEngine.delete_DolphinAccessor
    __del__ = lambda self: None
DolphinAccessor_swigregister = _PyDolphinMemoryEngine.DolphinAccessor_swigregister
DolphinAccessor_swigregister(DolphinAccessor)

def DolphinAccessor_init() -> "void":
    return _PyDolphinMemoryEngine.DolphinAccessor_init()
DolphinAccessor_init = _PyDolphinMemoryEngine.DolphinAccessor_init

def DolphinAccessor_hook() -> "void":
    return _PyDolphinMemoryEngine.DolphinAccessor_hook()
DolphinAccessor_hook = _PyDolphinMemoryEngine.DolphinAccessor_hook

def DolphinAccessor_unHook() -> "void":
    return _PyDolphinMemoryEngine.DolphinAccessor_unHook()
DolphinAccessor_unHook = _PyDolphinMemoryEngine.DolphinAccessor_unHook

def DolphinAccessor_readFromRAM(offset: 'u32 const', buffer: 'char *', size: 'size_t const', withBSwap: 'bool const') -> "bool":
    return _PyDolphinMemoryEngine.DolphinAccessor_readFromRAM(offset, buffer, size, withBSwap)
DolphinAccessor_readFromRAM = _PyDolphinMemoryEngine.DolphinAccessor_readFromRAM

def DolphinAccessor_writeToRAM(offset: 'u32 const', buffer: 'char const *', size: 'size_t const', withBSwap: 'bool const') -> "bool":
    return _PyDolphinMemoryEngine.DolphinAccessor_writeToRAM(offset, buffer, size, withBSwap)
DolphinAccessor_writeToRAM = _PyDolphinMemoryEngine.DolphinAccessor_writeToRAM

def DolphinAccessor_getPID() -> "int":
    return _PyDolphinMemoryEngine.DolphinAccessor_getPID()
DolphinAccessor_getPID = _PyDolphinMemoryEngine.DolphinAccessor_getPID

def DolphinAccessor_getEmuRAMAddressStart() -> "u64":
    return _PyDolphinMemoryEngine.DolphinAccessor_getEmuRAMAddressStart()
DolphinAccessor_getEmuRAMAddressStart = _PyDolphinMemoryEngine.DolphinAccessor_getEmuRAMAddressStart

def DolphinAccessor_getStatus() -> "DolphinComm::DolphinAccessor::DolphinStatus":
    return _PyDolphinMemoryEngine.DolphinAccessor_getStatus()
DolphinAccessor_getStatus = _PyDolphinMemoryEngine.DolphinAccessor_getStatus

def DolphinAccessor_enableMem2(doEnable: 'bool const') -> "void":
    return _PyDolphinMemoryEngine.DolphinAccessor_enableMem2(doEnable)
DolphinAccessor_enableMem2 = _PyDolphinMemoryEngine.DolphinAccessor_enableMem2

def DolphinAccessor_isMem2Enabled() -> "bool":
    return _PyDolphinMemoryEngine.DolphinAccessor_isMem2Enabled()
DolphinAccessor_isMem2Enabled = _PyDolphinMemoryEngine.DolphinAccessor_isMem2Enabled

def DolphinAccessor_autoDetectMem2() -> "void":
    return _PyDolphinMemoryEngine.DolphinAccessor_autoDetectMem2()
DolphinAccessor_autoDetectMem2 = _PyDolphinMemoryEngine.DolphinAccessor_autoDetectMem2

def DolphinAccessor_updateRAMCache() -> "Common::MemOperationReturnCode":
    return _PyDolphinMemoryEngine.DolphinAccessor_updateRAMCache()
DolphinAccessor_updateRAMCache = _PyDolphinMemoryEngine.DolphinAccessor_updateRAMCache

def DolphinAccessor_getFormattedValueFromCache(ramIndex: 'u32 const', memType: 'Common::MemType', memSize: 'size_t', memBase: 'Common::MemBase', memIsUnsigned: 'bool') -> "std::string":
    return _PyDolphinMemoryEngine.DolphinAccessor_getFormattedValueFromCache(ramIndex, memType, memSize, memBase, memIsUnsigned)
DolphinAccessor_getFormattedValueFromCache = _PyDolphinMemoryEngine.DolphinAccessor_getFormattedValueFromCache

def DolphinAccessor_copyRawMemoryFromCache(dest: 'char *', consoleAddress: 'u32 const', byteCount: 'size_t const') -> "void":
    return _PyDolphinMemoryEngine.DolphinAccessor_copyRawMemoryFromCache(dest, consoleAddress, byteCount)
DolphinAccessor_copyRawMemoryFromCache = _PyDolphinMemoryEngine.DolphinAccessor_copyRawMemoryFromCache

def DolphinAccessor_isValidConsoleAddress(address: 'u32 const') -> "bool":
    return _PyDolphinMemoryEngine.DolphinAccessor_isValidConsoleAddress(address)
DolphinAccessor_isValidConsoleAddress = _PyDolphinMemoryEngine.DolphinAccessor_isValidConsoleAddress

class IDolphinProcess(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDolphinProcess, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDolphinProcess, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _PyDolphinMemoryEngine.delete_IDolphinProcess
    __del__ = lambda self: None

    def findPID(self) -> "bool":
        return _PyDolphinMemoryEngine.IDolphinProcess_findPID(self)

    def findEmuRAMStartAddress(self) -> "bool":
        return _PyDolphinMemoryEngine.IDolphinProcess_findEmuRAMStartAddress(self)

    def readFromRAM(self, offset: 'u32 const', buffer: 'char *', size: 'size_t const', withBSwap: 'bool const') -> "bool":
        return _PyDolphinMemoryEngine.IDolphinProcess_readFromRAM(self, offset, buffer, size, withBSwap)

    def writeToRAM(self, offset: 'u32 const', buffer: 'char const *', size: 'size_t const', withBSwap: 'bool const') -> "bool":
        return _PyDolphinMemoryEngine.IDolphinProcess_writeToRAM(self, offset, buffer, size, withBSwap)

    def getPID(self) -> "int":
        return _PyDolphinMemoryEngine.IDolphinProcess_getPID(self)

    def getEmuRAMAddressStart(self) -> "u64":
        return _PyDolphinMemoryEngine.IDolphinProcess_getEmuRAMAddressStart(self)
IDolphinProcess_swigregister = _PyDolphinMemoryEngine.IDolphinProcess_swigregister
IDolphinProcess_swigregister(IDolphinProcess)


def dolphinAddrToOffset(addr: 'u32') -> "u32":
    return _PyDolphinMemoryEngine.dolphinAddrToOffset(addr)
dolphinAddrToOffset = _PyDolphinMemoryEngine.dolphinAddrToOffset

def offsetToDolphinAddr(offset: 'u32') -> "u32":
    return _PyDolphinMemoryEngine.offsetToDolphinAddr(offset)
offsetToDolphinAddr = _PyDolphinMemoryEngine.offsetToDolphinAddr
MemType_type_byte = _PyDolphinMemoryEngine.MemType_type_byte
MemType_type_halfword = _PyDolphinMemoryEngine.MemType_type_halfword
MemType_type_word = _PyDolphinMemoryEngine.MemType_type_word
MemType_type_float = _PyDolphinMemoryEngine.MemType_type_float
MemType_type_double = _PyDolphinMemoryEngine.MemType_type_double
MemType_type_string = _PyDolphinMemoryEngine.MemType_type_string
MemType_type_byteArray = _PyDolphinMemoryEngine.MemType_type_byteArray
MemType_type_num = _PyDolphinMemoryEngine.MemType_type_num
MemBase_base_decimal = _PyDolphinMemoryEngine.MemBase_base_decimal
MemBase_base_hexadecimal = _PyDolphinMemoryEngine.MemBase_base_hexadecimal
MemBase_base_octal = _PyDolphinMemoryEngine.MemBase_base_octal
MemBase_base_binary = _PyDolphinMemoryEngine.MemBase_base_binary
MemBase_base_none = _PyDolphinMemoryEngine.MemBase_base_none
MemOperationReturnCode_invalidInput = _PyDolphinMemoryEngine.MemOperationReturnCode_invalidInput
MemOperationReturnCode_operationFailed = _PyDolphinMemoryEngine.MemOperationReturnCode_operationFailed
MemOperationReturnCode_inputTooLong = _PyDolphinMemoryEngine.MemOperationReturnCode_inputTooLong
MemOperationReturnCode_invalidPointer = _PyDolphinMemoryEngine.MemOperationReturnCode_invalidPointer
MemOperationReturnCode_OK = _PyDolphinMemoryEngine.MemOperationReturnCode_OK

def getSizeForType(type: 'Common::MemType const', length: 'size_t const') -> "size_t":
    return _PyDolphinMemoryEngine.getSizeForType(type, length)
getSizeForType = _PyDolphinMemoryEngine.getSizeForType

def shouldBeBSwappedForType(type: 'Common::MemType const') -> "bool":
    return _PyDolphinMemoryEngine.shouldBeBSwappedForType(type)
shouldBeBSwappedForType = _PyDolphinMemoryEngine.shouldBeBSwappedForType

def formatStringToMemory(returnCode: 'Common::MemOperationReturnCode &', actualLength: 'size_t &', inputString: 'std::string const', base: 'Common::MemBase const', type: 'Common::MemType const', length: 'size_t const') -> "char *":
    return _PyDolphinMemoryEngine.formatStringToMemory(returnCode, actualLength, inputString, base, type, length)
formatStringToMemory = _PyDolphinMemoryEngine.formatStringToMemory

def formatMemoryToString(memory: 'char const *', type: 'Common::MemType const', length: 'size_t const', base: 'Common::MemBase const', isUnsigned: 'bool const', withBSwap: 'bool const'=False) -> "std::string":
    return _PyDolphinMemoryEngine.formatMemoryToString(memory, type, length, base, isUnsigned, withBSwap)
formatMemoryToString = _PyDolphinMemoryEngine.formatMemoryToString
# This file is compatible with both classic and new-style classes.

cvar = _PyDolphinMemoryEngine.cvar
MEM1_SIZE = cvar.MEM1_SIZE
MEM1_START = cvar.MEM1_START
MEM1_END = cvar.MEM1_END
MEM2_SIZE = cvar.MEM2_SIZE
MEM2_START = cvar.MEM2_START
MEM2_END = cvar.MEM2_END

