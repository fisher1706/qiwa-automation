from __future__ import annotations

from typing import TypeVar

from utils.assertion.assertion_types import AssertionTypes

T = TypeVar("T")


class AssertionBase:
    def __init__(self, actual: T):
        self.actual = actual
        self.description: str = ""

    def assert_(self, actual: T, expected: T, assertion: AssertionTypes, step) -> AssertionBase:
        operator, context = assertion.value
        error_message = self._error_template(actual, expected, context)
        with step:
            assert operator(actual, expected), error_message
        return self

    def _error_template(self, actual: T, expected: T, context: str) -> str:
        return f"""
            Checking: {self.description}
            Expected: {expected} {type(expected)}
            Actual: {actual} {type(actual)}
    
            Expression: assert {actual} {context} {expected}
            """

    def as_(self, description: str) -> AssertionBase:
        self.description = description
        return self
