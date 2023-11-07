import operator
from enum import Enum


def in_(a, b):
    return a in b


class AssertionTypes(Enum):
    EQUAL = operator.eq, "=="
    NOT_EQUAL = operator.ne, "!="
    CONTAINS = operator.contains, "contains"
    IN = in_, "in"
