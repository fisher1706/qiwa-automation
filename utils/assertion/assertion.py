from typing import TypeVar

from utils.assertion.assertion_mixin import AssertionMixin

T = TypeVar("T")


def assert_that(actual: T) -> AssertionMixin:
    assertion = AssertionMixin(actual=actual)
    return assertion


def assert_status_code(code: int) -> AssertionMixin:
    assertion = AssertionMixin(actual=code)
    return assertion.as_("status code")
