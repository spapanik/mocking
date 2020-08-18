def echo(*args):
    return args


def call_id_builtin(obj):
    return id(obj)


def call_same_module_function(*args):
    return echo(*args)
