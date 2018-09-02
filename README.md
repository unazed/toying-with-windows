# toying-with-windows
i can't even

A simple implementation and abstraction onto the Windows API for functions varying over the user32.dll and kernel32.dll libraries thus-far. Currently supported functions are:
- MessageBox{A/W} a.b.:\* `messagebox(caption, body, type_input=0x00)`
- GetClipboardData a.b.: `get_clipboard_data(format_)`
- OpenClipboard a.b.: `open_clipboard(new_window_owner)`
- CloseClipboard a.b.: `close_clipboard()`
- GetLastError a.b.: `get_last_error()`
- SetLastError a.b.: `set_last_error(error_code)`
- SetPhysicalCursorPos a.b.: `set_physical_cursor_pos(x, y)`
- GetPhysicalCursorPos a.b.: `get_physical_cursor_pos(point**)`
- GetStdHandle a.b.: `get_std_handle(std_handle)`
- WriteConsole{A/W} a.b.: `write_console(handle, data)`
- SetConsoleTitle a.b.: `set_console_title(name)`
- ReadConsole a.b.: `read_console(handle, data_pointer, read_count)`
- GetSystemMetrics a.b.: `get_system_metrics(idx)`
- GetComputerName a.b.: `get_computer_name(data_pointer)`
- GetComputerNameEx a.b.: `get_computer_name_ex(name_type, data_pointer)`

\* => 'aliased by'

\*\* => `point` is a `ctypes.pointer` to an instantiated `POINT` structure (defined in the file)

The general format of the functions only specifies a `_ctypes_configuration` customization parameter which allows for run-time customization of compile-time set variables, for instance in the `messagebox` function; for further simplicity the `hWnd` parameter is not specified by the caller; it is within the pseudo-dictionary `_ctypes_configuration`. A call-parameter is defined as the following format: `(<param-name>, (<ctypes-type>, <true-if-python-passed-param-else-this-is-used>))`.
There are five primary helper functions used within the implementation of such WinAPI functions, namely: `import_winapi_function`, `create_string`, `argtypes_from_ctypes_configuration`, `ctypes_configuration_param_select` and `debug_fn`. `import_winapi_function` is defined as: `import_winapi_function(namespace, name, argtypes, restype, is_unicode=UNICODE)`, namespace refers to the certain library under which the function should be looked for, name is the function name under that namespace, argtypes is an iterable which contains an ordered list of argument types correspondent to the WinAPI definition, restype is also the corresponding return type; essentially, the importer firstly looks for W\[idechar\] or A\[SCII\] types of functions depending on `is_unicode`-- afterwards, if the function does not exist with an A/W type then the generic unbiased function name is retrieved at the expense of a try/except clause. These function names are cached in a dictionary for quicker, later retrieval.
`create_string` returns a pointer to an initalized ASCII/Unicode string for use in functions requiring LP\[T\]CSTR or alike parameters.
`argtypes_from_ctypes_configuration` is a helper for retrieving argument types from `_ctypes_configuration`-like structures.
`ctypes_configuration_param_select` is a quite confusing function code-wise, but it, essentially, allows you in practice to see whether a `_ctypes_configuration` parameter implies that the parameter is passed within the Python function or statically encoded within the configuration; allowing for the syntax of `ctypes_configuration_param_select(config, param_idx) or python_passed_param` where `ctypes_configuration_param_select(config, param_idx)` returns the encoded parameter.
`debug_fn` is a trivial function allowing for cleaner syntax when wanting to debug the error-state before/after a function call and its return value; it returns the return value.
