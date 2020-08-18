def echo(*args):
    return args


def call_print_builtin():
    print("actual string")


def call_same_module_function(*args):
    return echo(*args)
