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
UNICODE = True

function_cache = {}


def import_winapi_function(namespace, name, argtypes, restype, is_unicode=UNICODE):
    name += "W" if is_unicode else "A"
    qual_fn_name = f"{namespace}.{name}"
    if qual_fn_name in function_cache:
        return function_cache[qual_fn_name]
    fn = getattr(namespace, name)
    fn.argtypes = argtypes
    fn.restype = restype
    function_cache[qual_fn_name] = fn
    return fn

def create_string(string, unicode=False):
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
    message_box(_ctypes_configuration[0][1][1],  # hWnd
                ctypes_configuration_param_select(_ctypes_configuration, 1) or body,
                ctypes_configuration_param_select(_ctypes_configuration, 2) or caption,
                ctypes_configuration_param_select(_ctypes_configuration, 3) or type_input)
                
