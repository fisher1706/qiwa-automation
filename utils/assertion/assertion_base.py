from __future__ import annotations

from typing import Callable, Optional, TypeVar

import allure

from utils.assertion.assertion_types import AssertionTypes

T = TypeVar("T")


class AssertionBase:
    def __init__(self, actual: T, decorator: Optional[Callable] = None):
        self.actual = actual
        self._description: str = ""
        self._decorator = decorator

    def _assert(self, expected: T, method: AssertionTypes) -> AssertionBase:
        operator, context = method.value
        step_name = f'Assert that {self._description} {context} "{expected}"'
        error_message = self._error_template(expected, context)
        with allure.step(step_name):
            self._decorator(
                self._perform_assertion(operator, expected, error_message)
            ) if self._decorator else self._perform_assertion(operator, expected, error_message)
            return self

    def _perform_assertion(self, operator: Callable, expected: T, message: str) -> None:
        assert operator(self.actual, expected), message

    def _error_template(self, expected: T, context: str) -> str:
        return f"""
        Checking: {self._description}
        Expected: {expected} {type(expected)}
        Actual: {self.actual} {type(self.actual)}

        Expression: assert {self.actual} {context} {expected}
        """

    def as_(self, description: str) -> AssertionBase:
        self._description = description
        return self
