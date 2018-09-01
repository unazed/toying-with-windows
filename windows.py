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

UNICODE = True

function_cache = {}

class POINT(ctypes.Structure):
    _fields_ = [
            ("x", ctypes.c_long),
            ("y", ctypes.c_long)
            ]

def import_winapi_function(namespace, name, argtypes, restype, is_unicode=UNICODE):
    name += "W" if is_unicode else "A"
    qual_fn_name = f"{namespace}.{name}"
    if qual_fn_name in function_cache:
        return function_cache[qual_fn_name]
    try:
        fn = getattr(namespace, name)
    except AttributeError:
        qual_fn_name = qual_fn_name[:-1]
        fn = getattr(namespace, name[:-1])  # non-ansi/unicode fn.
    fn.argtypes = argtypes
    fn.restype = restype
    function_cache[qual_fn_name] = fn
    return fn

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

def display_messagebox(caption, body, type_input=0x00,
                       _ctypes_configuration=(
                        ("hWnd",      (ctypes.c_voidp, None)),
                        ("lpText",    (ctypes.POINTER(ctypes.c_wchar), True)),
                        ("lpCaption", (ctypes.POINTER(ctypes.c_wchar), True)),
                        ("uType",     (ctypes.c_uint, True))
                       )):
    message_box = import_winapi_function(
        ctypes.windll.user32,
        "MessageBox",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_int
    )
    return message_box(_ctypes_configuration[0][1][1],  # hWnd
        ctypes_configuration_param_select(_ctypes_configuration, 1) or body,
        ctypes_configuration_param_select(_ctypes_configuration, 2) or caption,
        ctypes_configuration_param_select(_ctypes_configuration, 3) or type_input)

def get_clipboard_data(format_, _ctypes_configuration=(
                       ("uFormat", (ctypes.c_uint, True)), 
                      )):
    get_clipboard_data = import_winapi_function(
        ctypes.windll.user32,
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
        ctypes.windll.user32,
        "OpenClipboard",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return open_clipboard(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or new_window_owner
    )

def get_last_error(_ctypes_configuration=()):
    get_last_error = import_winapi_function(
        ctypes.windll.kernel32,
        "GetLastError",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ulong
    )
    return get_last_error()

def set_last_error(error_code, _ctypes_configuration=(
                   ("dwErrorCode", (ctypes.c_ulong, True)),
                  )):
    set_last_error = import_winapi_function(
        ctypes.windll.kernel32,
        "SetLastError",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        None
    )
    return set_last_error(
        ctypes_configuration_param_select(_ctypes_configuration, 0) or error_code
    )

def set_physical_cursor_pos(x, y, _ctypes_configuration=(
                            ("X", (ctypes.c_int, True)),
                            ("Y", (ctypes.c_int, True))
                           )):
    set_physical_cursor_pos = import_winapi_function(
        ctypes.windll.user32,
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
        ctypes.windll.user32,
        "CloseClipboard",
        argtypes_from_ctypes_configuration(_ctypes_configuration),
        ctypes.c_ushort
    )
    return close_clipboard()

def get_physical_cursor_pos(point, _ctypes_configuration=(
                            ("lpPoint", (ctypes.POINTER(POINT), True)), 
                           )):
    get_physical_cursor_pos = import_winapi_function(
        ctypes.windll.user32,
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


if __name__ == "__main__":
    clicked = debug_fn(display_messagebox,
                       create_string("hello"),
                       create_string("from the other side"),
                       MESSAGEBOX_INPUTS["MB_ABORTRETRYIGNORE"])

    if debug_fn(open_clipboard, None):
        print("Successfully opened a clipboard handle.")

    if debug_fn(set_physical_cursor_pos, 69, 69):
        print("Successfully set the cursor position to (69, 69)")

    point = ctypes.pointer(POINT())
    if debug_fn(get_physical_cursor_pos, point):
        print(f"Successfully stored cursor position point.x={point.contents.x} point.y={point.contents.y}")

    data_handle = debug_fn(get_clipboard_data, 0x01)  # CF_TEXT
    print(f"Clipboard (ANSI/ASCII) contents: {repr(ctypes.string_at(data_handle).decode())}")

    if debug_fn(close_clipboard):
        print("Successfully closed the clipboard.")
 
    print("complete.")
                 
