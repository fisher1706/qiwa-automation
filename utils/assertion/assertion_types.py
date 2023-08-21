import operator
from enum import Enum
from typing import Any


def contains(left: Any, right: Any) -> bool:
    """Same as ``left in right``"""
    return left in right


def length(left: Any, right: Any) -> bool:
    """Same as ``len(left) == len(right)``"""
    return len(left) == right


class AssertionTypes(Enum):
    EQUAL = operator.eq, "=="
    NOT_EQUAL = operator.ne, "!="
    IN_ = contains, "is in"
    LENGTH = length, "length is"
