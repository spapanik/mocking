from typing import TypeVar

T = TypeVar("T")


def method(*args: T) -> tuple[T, ...]:
    return args  # pragma: no cover
