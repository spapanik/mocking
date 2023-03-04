from typing import TypeVar

from mocking.library import method

T = TypeVar("T")


def division(numerator: int, denominator: int) -> float:
    return numerator / denominator


def echo(*args: T) -> tuple[T, ...]:
    return args  # pragma: no cover


def call_id_builtin(obj: object) -> int:
    return id(obj)


def call_same_module_function(*args: T) -> tuple[T, ...]:
    return echo(*args)


def call_library_module_function(*args: T) -> tuple[T, ...]:
    return method(*args)
