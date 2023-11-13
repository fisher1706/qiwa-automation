import operator
from enum import Enum


def in_(a, b):
    return a in b


class AssertionTypes(Enum):
    EQUAL = operator.eq, "=="
    NOT_EQUAL = operator.ne, "!="
    GREATER_OR_EQUAL = operator.ge, ">="
    LESS_OR_EQUAL = operator.le, "<="
    CONTAINS = operator.contains, "contains"
    IN = in_, "in"
