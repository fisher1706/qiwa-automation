import operator
from enum import Enum


class AssertionTypes(Enum):
    EQUAL = operator.eq, "=="
    NOT_EQUAL = operator.ne, "!="
    CONTAINS = operator.contains, "contains"
