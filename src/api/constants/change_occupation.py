from enum import Enum


class NonEligibilityReasons(str, Enum):
    NOT_ALLOWED = "Sorry, it is not allowed to change from the current occupation."
