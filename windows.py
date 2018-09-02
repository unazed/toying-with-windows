import ctypes


MESSAGEBOX_INPUTS = {
    "MB_ABORTRETRYIGNORE":  0x00000002,
    "MB_CANCELTRYCONTINUE": 0x00000006,
    "MB_HELP":              0x00004000,
    "MB_OK":                0x00000000,
    "MB_OKCANCEL":          0x00000001,
    "MB_RETRYCANCEL":       0x00000005,
    "MB_YESNO":             0x00000004,
    "MB_YESNOCANCEL":       0x00000003,
    }
MESSAGEBOX_RETCODE = {
    3:  "IDABORT",
    2:  "IDCANCEL",
    11: "IDCONTINUE",
    5:  "IDIGNORE",
    7:  "IDNO",
    1:  "IDOK",
    4:  "IDRETRY",
    10: "IDTRYAGAIN",
    6:  "IDYES"
    }
STD_CLIPBOARD_FORMATS = {
    "CF_BITMAP":          2,
    "CF_DIB":             8,
    "CF_DIBV5":           17,
    "CF_DIF":             5,
    "CF_DSPBITMAP":       0x82,
    "CF_DSENHMETAFILE":   0x8E,
    "CF_DSPMETAFILEPICT": 0x83,
    "CF_DSPTEXT":         0x81,
    "CF_ENHMETAFILE":     14,
    "CF_GDIOBJFIRST":     0x300,
    "CF_GDIOBJLAST":      0x3FF,
    "CF_HDROP":           15,
    "CF_LOCALE":          16,
    "CF_METAFILEPICT":    3,
    "CF_OEMTEXT":         7,
    "CF_OWNERDISPLAY":    0x80,
    "CF_PALETTE":         9,
    "CF_PENDATA":         10,
    "CF_PRIVATEFIRST":    0x200,
    "CF_PRIVATELAST":     0x2FF,
    "CF_RIFF":            11,
    "CF_SYLK":            4,
    "CF_TEXT":            1,
    "CF_TIFF":            6,
    "CF_UNICODETEXT":     13,
    "CF_WAVE":            12
    }
SYS_METRICS_INDICES = {
    "SM_ARRANGE":                     56,
    "SM_CLEANBOOT":                   67,
    "SM_CMONITORS":                   80,
    "SM_CMOUSEBUTTONS":               43,
    "SM_CONVERTIBLESLATEMODE":        0x2003,
    "SM_CXBORDER":                    5,
    "SM_CXCURSOR":                    13,
    "SM_CXDLGFRAME":                  7,
    "SM_CXDOUBLECLK":                 36,
    "SM_CXDRAG":                      68,
    "SM_CXEDGE":                      45,
    "SM_CXFIXEDFRAME":                7,
    "SM_CXFOCUSBORDER":               83,
    "SM_CXFRAME":                     32,
    "SM_CXFULLSCREEN":                16,
    "SM_CXHSCROLL":                   21,
    "SM_CXHTHUMB":                    10,
    "SM_CXICON":                      11,
    "SM_CXICONSPACING":               38,
    "SM_CXMAXIMIZED":                 61,
    "SM_CXMAXTRACK":                  59,
    "SM_CXMENUCHECK":                 71,
    "SM_CXMENUSIZE":                  54,
    "SM_CXMIN":                       28,
    "SM_CXMINIMIZED":                 57,
    "SM_CXMINSPACING":                47,
    "SM_CXMINTRACK":                  34,
    "SM_CXPADDEDBORDER":              92,
    "SM_CXSCREEN":                    0,
    "SM_CXSIZE":                      30,
    "SM_CXSIZEFRAME":                 32,
    "SM_CXSMICON":                    49,
    "SM_CXSMSIZE":                    52,
    "SM_CXVIRTUALSCREEN":             78,
    "SM_CXVSCROLL":                   2,
    "SM_CYBORDER":                    6,
    "SM_CYCAPTION":                   4,
    "SM_CYCURSOR":                    14,
    "SM_CYDLGFRAME":                  8,
    "SM_CYDOUBLECLK":                 37,
    "SM_CYDRAG":                      69,
    "SM_CYEDGE":                      46,
    "SM_CYFIXEDFRAME":                8,
    "SM_CYFOCUSBORDER":               84,
    "SM_CYFRAME":                     33,
    "SM_CYFULLSCREEN":                17,
    "SM_CYHSCROLL":                   3,
    "SM_CYICON":                      12,
    "SM_CYICONSPACING":               39,
    "SM_CYKANJIWINDOW":               18,
    "SM_CYMAXIMIZED":                 62,
    "SM_CYMAXTRACK":                  60,
    "SM_CYMENU":                      16,
    "SM_CYMENUCHECK":                 72,
    "SM_CYMENUSIZE":                  55,
    "SM_CYMIN":                       29,
    "SM_CYMINIMIZED":                 58,
    "SM_CYMINSPACING":                48,
    "SM_CYMINTRACK":                  35,
    "SM_CYSCREEN":                    1,
    "SM_CYSIZE":                      31,
    "SM_CYSIZEFRAME":                 33,
    "SM_CYSMCAPTION":                 51,
    "SM_CYSMICON":                    50,
    "SM_CYSMSIZE":                    53,
    "SM_CYVIRTUALSCREEN":             79,
    "SM_CYVSCROLL":                   20,
    "SM_CYVTHUMB":                    9,
    "SM_DBCSENABLED":                 42,
    "SM_DEBUG":                       22,
    "SM_DIGITIZER":                   94,
    "SM_IMMENALED":                   82,
    "SM_MAXIMUMTOUCHES":              95,
    "SM_MEDIACENTER":                 87,
    "SM_MENUDROPALIGNMENT":           40,
    "SM_MIDEASTENABLED":              74,
    "SM_MOUSEPRESENT":                19,
    "SM_MOUSEHORIZONTALWHEELPRESENT": 91,
    "SM_MOUSEWHEELPRESENT":           75,
    "SM_NETWORK":                     63,
    "SM_PENWINDOWS":                  41,
    "SM_REMOTECONTROL":               0x2001,
    "SM_REMOTESESSION":               0x1000,
    "SM_SAMEDISPLAYFORMAT":           81,
    "SM_SECURE":                      44,
    "SM_SERVERR2":                    89,
    "SM_SHOWSOUNDS":                  70,
    "SM_SHUTTINGDOWN":                0x2000,
    "SM_SLOWMACHINE":                 73,
    "SM_STARTER":                     88,
    "SM_SWAPBUTTON":                  23,
    "SM_SYSTEMDOCKED":                0x2004,
    "SM_TABLETPC":                    86,
    "SM_XVIRTUALSCREEN":              76,
    "SM_YVIRTUALSCREEN":              77
    }
COMPUTER_NAME_FORMAT = {v: k for k, v in enumerate([
    "ComputerNameNetBIOS",
    "ComputerNameDnsHostname",
    "ComputerNameDnsDomain",
    "ComputerNameDnsFullyQualified",
    "ComputerNamePhysicalNetBIOS",
    "ComputerNamePhysicalDnsHostname",
    "ComputerNamePhysicalDnsDomain",
    "ComputerNamePhysicalDnsFullyQualified",
    "ComputerNameMax"  # unused
    ])}

UNICODE = True
TCHAR = ctypes.c_wchar if UNICODE else ctypes.c_char
MAX_PATH = 260
function_cache = {
        "kernel32.GetProcAddress": ctypes.windll.kernel32.GetProcAddress,
        "kernel32.SetLastError": ctypes.windll.kernel32.SetLastError,
        "kernel32.GetModuleHandleA": ctypes.windll.kernel32.GetModuleHandleA,
        "kernel32.GetLastError": ctypes.windll.kernel32.GetLastError
        }  # primitive definitions, not WinAPIFunction instances

function_cache['kernel32.GetProcAddress'].argtypes = (
    ctypes.c_voidp,
    ctypes.POINTER(ctypes.c_char)
)
function_cache['kernel32.GetProcAddress'].restype = ctypes.c_voidp

function_cache['kernel32.SetLastError'].argtypes = (
    ctypes.c_ulong,
)
function_cache['kernel32.SetLastError'].restype = None

function_cache['kernel32.GetModuleHandleA'].argtypes = (
    ctypes.POINTER(ctypes.c_char),
)
function_cache['kernel32.GetModuleHandleA'].restype = ctypes.c_voidp

function_cache['kernel32.GetLastError'].argtypes = ()
function_cache['kernel32.GetLastError'].restype = ctypes.c_ulong

len_pointer = lambda data, ctype: ctypes.pointer(ctype(len(data)))

class WinAPIFunction(object):
    def __init__(self, module, name, handle, restype, argtypes):
        self.module = module
        self.name = name
        self.handle = handle
        self.argtypes = argtypes
        self.restype = restype 
    def __repr__(self):
        return f"<{self.module}.{self.name} @ {hex(self.handle)}>"
    __str__ = __repr__
    def __call__(self, *args):
        return ctypes.WINFUNCTYPE(self.restype, *self.argtypes)(self.handle)(*args)

class POINT(ctypes.Structure):
    _fields_ = [
            ("x", ctypes.c_long),
            ("y", ctypes.c_long)
            ]

class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
            ("dwSize",              ctypes.c_ulong),
            ("cntUsage",            ctypes.c_ulong),
            ("th32ProcessID",       ctypes.c_ulong),
            ("th32DefaultHeapID",   ctypes.POINTER(ctypes.c_ulong)),
            ("th32ModuleID",        ctypes.c_ulong),
            ("cntThreads",          ctypes.c_ulong),
            ("th32ParentProcessID", ctypes.c_ulong),
            ("pcPriClassBase",      ctypes.c_long),
            ("dwFlags",             ctypes.c_ulong),
            ("szExeFile",           ctypes.c_char*MAX_PATH)
            ]

def import_winapi_function(namespace, name, argtypes, restype, is_unicode=UNICODE):
    gle = function_cache['kernel32.GetLastError']
    sle = function_cache['kernel32.SetLastError']
    gpa = function_cache['kernel32.GetProcAddress']
    gmh = function_cache['kernel32.GetModuleHandleA']

    name += "W" if is_unicode else "A"
    qual_fn_name = f"{namespace}.{name}"
    if qual_fn_name in function_cache:
        return function_cache[qual_fn_name]
    namespace_handle = gmh(create_string(namespace, False))
    if gle() == 127:
        sle(0)
        raise LookupError(f"Module: {namespace} doesn't exist.")
    function_handle = gpa(namespace_handle, create_string(name, False))
    if gle() != 127:
        function_cache[qual_fn_name] = WinAPIFunction(namespace, name, function_handle, restype, argtypes)
        return function_cache[qual_fn_name]
    sle(0) 
    name = name[:-1]
    qual_fn_name = qual_fn_name[:-1]
    if qual_fn_name in function_cache:
        return function_cache[qual_fn_name]
    function_handle = gpa(namespace_handle, create_string(name, False))
    if gle() == 127:
        sle(0)
        raise LookupError(f"Function: {namespace}.{name} doesn't exist.")
    function_cache[qual_fn_name] = WinAPIFunction(namespace, name, function_handle, restype, argtypes)
    return function_cache[qual_fn_name]

def create_string(string, unicode=UNICODE):
    if not unicode:
        pointer = ctypes.create_string_buffer(len(string)+1)
        pointer.value = string.encode()
    else:
        pointer = ctypes.create_unicode_buffer(len(string)+1)
        pointer.value = string
    return pointer

def argtypes_from_ctypes_configuration(ctypes_configuration):
    return tuple(v[0] for _, v in ctypes_configuration)

def ctypes_configuration_param_select(ctypes_configuration, idx):
    return ctypes_configuration[idx][1][1] if ctypes_configuration[idx][1][1] is not True else False

# for the _ctypes_configuration parameter, the following is the format:
## (
##   (<winapi-param-name>, (
##                           <corresponding-ctypes-type>,
##                           <true-if-given-by-function-else-value>
##                         )),
##   ...
## )

def messagebox(caption, body, type_input=0x00,
                       _ctypes_configuration=(
                        ("hWnd",      (ctypes.c_voidp, None)),
                        ("lpText",    (ctypes.POINTER(ctypes.c_wchar), True)),
                        ("lpCaption", (ctypes.POINTER(ctypes.c_wchar), True)),
                        ("uType",     (ctypes.c_uint, True))
                       )):
    message_box = import_winapi_function(
        "user32",
        "MessageBox",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_int
    )
    return message_box(_ctypes_configuration[0][1][1],  # hWnd
        ctypes_configuration_param_select(_ctypes_configuration, 1) or body,
        ctypes_configuration_param_select(_ctypes_configuration, 2) or caption,
        ctypes_configuration_param_select(_ctypes_configuration, 3) or type_input
    )

def get_clipboard_data(format_, _ctypes_configuration=(
                       ("uFormat", (ctypes.c_uint, True)), 
                      )):
    get_clipboard_data = import_winapi_function(
        "user32",
        "GetClipboardData",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_voidp
    )
    return get_clipboard_data(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or format_
    )

def open_clipboard(new_window_owner, _ctypes_configuration=(
                   ("hWndNewOwner", (ctypes.c_voidp, True)),
                  )):
    open_clipboard = import_winapi_function(
        "user32",
        "OpenClipboard",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return open_clipboard(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or new_window_owner
    )

def get_last_error(_ctypes_configuration=()):
    return function_cache['kernel32.GetLastError']()

def set_last_error(error_code, _ctypes_configuration=(
                   ("dwErrorCode", (ctypes.c_ulong, True)),
                  )):
    return function_cache['kernel32.SetLastError'](
        ctypes_configuration_param_select(_ctypes_configuration, 0) or error_code
    )

def set_physical_cursor_pos(x, y, _ctypes_configuration=(
                            ("X", (ctypes.c_int, True)),
                            ("Y", (ctypes.c_int, True))
                           )):
    set_physical_cursor_pos = import_winapi_function(
        "user32",
        "SetPhysicalCursorPos",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return set_physical_cursor_pos(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or x,
        ctypes_configuration_param_select(_ctypes_configuration, 1) or y
    )

def close_clipboard(_ctypes_configuration=()):
    close_clipboard = import_winapi_function(
        "user32",
        "CloseClipboard",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return close_clipboard()

def get_physical_cursor_pos(point, _ctypes_configuration=(
                            ("lpPoint", (ctypes.POINTER(POINT), True)), 
                           )):
    get_physical_cursor_pos = import_winapi_function(
        "user32",
        "GetPhysicalCursorPos",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return get_physical_cursor_pos(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or point
    )

def debug_fn(fn, *args, **kwargs):
    gle = get_last_error  # changeable
    print(f"\n{fn}:")
    print(f"\tget_last_error: {gle()}")
    res = fn(*args, **kwargs)
    print(f"\tret. code: {res}")
    print(f"\tget_last_error: {gle()}\n")
    return res

def get_std_handle(std_handle, _ctypes_configuration=(
                   ("nStdHandle", (ctypes.c_ulong, True)),
                  )):
    get_std_handle = import_winapi_function(
        "kernel32",
        "GetStdHandle",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_voidp
    )
    return get_std_handle(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or std_handle
    )

def write_console(handle, data, _ctypes_configuration=(
                  ("hConsoleOutput", (ctypes.c_voidp, True)),
                  ("lpBuffer", (ctypes.c_voidp, True)),
                  ("nNumberOfCharsToWrite", (ctypes.c_ulong, lambda data: len(data.value))),
                  ("lpNumberOfCharsWritten", (ctypes.POINTER(ctypes.c_ulong), lambda: ctypes.pointer(ctypes.c_ulong()))),
                  ("lpReserved", (ctypes.c_voidp, None))
                 )):
    write_console = import_winapi_function(
        "kernel32",
        "WriteConsole",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return write_console(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or handle,
        ctypes_configuration_param_select(_ctypes_configuration, 1) or data,
        _ctypes_configuration[2][1][1](data),
        _ctypes_configuration[3][1][1](),
        _ctypes_configuration[4][1][1]
    )

def set_console_title(name, _ctypes_configuration=(
                      ("lpConsoleTitle", (ctypes.POINTER(ctypes.c_wchar), True)),
                     )):
    set_console_title = import_winapi_function(
        "kernel32",
        "SetConsoleTitle",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return set_console_title(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or name
    )

def read_console(handle, data_pointer, read_count, _ctypes_configuration=(
                 ("hConsoleInput", (ctypes.c_voidp, True)),
                 ("lpBuffer", (ctypes.c_voidp, True)),
                 ("nNumberOfCharsToRead", (ctypes.c_ulong, True)),
                 ("lpNumberOfCharsRead", (ctypes.c_voidp, lambda: ctypes.pointer(ctypes.c_ulong()))),
                 ("pInputControl", (ctypes.c_voidp, None))
                )):
    read_console = import_winapi_function(
        "kernel32",
        "ReadConsole",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return read_console(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or handle,
        ctypes_configuration_param_select(_ctypes_configuration, 1) or data_pointer,
        ctypes_configuration_param_select(_ctypes_configuration, 2) or read_count,
        _ctypes_configuration[3][1][1](),
        _ctypes_configuration[4][1][1]
    )

def get_system_metrics(idx, _ctypes_configuration=(
                       ("nIndex", (ctypes.c_int, True)),
                      )):
    get_system_metrics = import_winapi_function(
        "user32",
        "GetSystemMetrics",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_int
    )
    return get_system_metrics(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or idx
    )

def get_computer_name(data_pointer, _ctypes_configuration=(
                      ("lpBuffer", (ctypes.POINTER(TCHAR), True)),
                      ("nSize", (ctypes.POINTER(ctypes.c_ulong), lambda d: len_pointer(d, ctypes.c_ulong)))
                     )):
    get_computer_name = import_winapi_function(
        "kernel32",
        "GetComputerName",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    d = ctypes_configuration_param_select(_ctypes_configuration, 0) or data_pointer
    # prevent repetition
    return get_computer_name(
        d,
        _ctypes_configuration[1][1][1](d)
    )

def get_computer_name_ex(name_type, data_pointer, _ctypes_configuration=(
                         ("NameType", (ctypes.c_uint, True)),
                         ("lpBuffer", (ctypes.POINTER(TCHAR), True)),
                         ("lpnSize", (ctypes.POINTER(ctypes.c_ushort), lambda d: len_pointer(d, ctypes.c_ushort)))
                        )):
    get_computer_name_ex = import_winapi_function(
        "kernel32",
        "GetComputerNameEx",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_int
    )
    return get_computer_name_ex(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or name_type,
        ctypes_configuration_param_select(_ctypes_configuration, 1) or data_pointer,
        _ctypes_configuration[2][1][1](data_pointer)
    )

def open_process(access, inherit_handle, pid, _ctypes_configuration=(
                 ("dwDesiredAccess", (ctypes.c_ulong, True)),
                 ("bInheritHandle", (ctypes.c_int, True)),
                 ("dwProcessId", (ctypes.c_ulong, True))
                )):
    open_process = import_winapi_function(
        "kernel32",
        "OpenProcess",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_voidp
    )
    return open_process(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or access,
        ctypes_configuration_param_select(_ctypes_configuration, 1) or inherit_handle,
        ctypes_configuration_param_select(_ctypes_configuration, 2) or pid
    )

def create_toolhelp32_snapshot(flags, pid, _ctypes_configuration=(
                               ("dwflags", (ctypes.c_ulong, True)),
                               ("th32ProcessID", (ctypes.c_ulong, True))
                              )):
    create_toolhelp32_snapshot = import_winapi_function(
        "kernel32",
        "CreateToolhelp32Snapshot",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_voidp
    )
    print(create_toolhelp32_snapshot)
    return create_toolhelp32_snapshot(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or flags,
        ctypes_configuration_param_select(_ctypes_configuration, 1) or pid
    )

def process32_first(snapshot_handle, process_entry_pointer, _ctypes_configuration=(
                    ("hSnapshot", (ctypes.c_voidp, True)),
                    ("lppe", (ctypes.POINTER(PROCESSENTRY32), True))
                   )):
    process32_first = import_winapi_function(
        "kernel32",
        "Process32First",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_int
    )
    return process32_first(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or snapshot_handle,
        ctypes_configuration_param_select(_ctypes_configuration, 1) or process_entry_pointer
    )

def get_module_handle_ascii(module_name, _ctypes_configuration=(
                      ("lpModuleName", (ctypes.POINTER(ctypes.c_char), True)),
                     )):
    return function_cache['kernel32.GetModuleHandleA'](
        ctypes_configuration_param_select(_ctypes_configuration, 0) or module_name
    )

def get_module_handle_unicode(module_name, _ctypes_configuration=(
                              ("lpModuleName", (ctypes.POINTER(ctypes.c_wchar), True)),
                             )):
    get_module_handle = import_winapi_function(
        "kernel32",
        "GetModuleHandleW",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_voidp
    )
    return get_module_handle(
        _ctypes_configuration_param_select(_ctypes_configuration, 0) or module_name
    )

def get_proc_address(module_handle, fn_name, _ctypes_configuration=(
                     ("hModule", (ctypes.c_voidp, True)),
                     ("lpProcName", (ctypes.POINTER(ctypes.c_char), True))
                    )):
    return function_cache['kernel32.GetProcAddress'](
        ctypes_configuration_param_select(_ctypes_configuration, 0) or module_handle,
        ctypes_configuration_param_select(_ctypes_configuration, 1) or fn_name
    )

if __name__ == "__main__":
    messagebox(create_string("hey"), create_string("there"))

