from __future__ import annotations

from typing import TypeVar

import allure

from utils.assertion.assertion_types import AssertionTypes

T = TypeVar("T")


class AssertionBase:
    def __init__(self, actual: T):
        self.actual = actual
        self._description: str = ""

    def assert_(
        self, actual: T, expected: T, assertion: AssertionTypes, allure_title: str
    ) -> AssertionBase:
        operator, context = assertion.value
        error_message = self._error_template(actual, expected, context)
        with allure.step(f"Assert that {self._description} {allure_title} {expected}"):
            assert operator(actual, expected), error_message
        return self

    def _error_template(self, actual: T, expected: T, context: str) -> str:
        return f"""
            Checking: {self._description}
            Expected: {expected} {type(expected)}
            Actual: {actual} {type(actual)}
    
            Expression: assert {actual} {context} {expected}
            """

    def as_(self, description: str) -> AssertionBase:
        self._description = description
        return self
