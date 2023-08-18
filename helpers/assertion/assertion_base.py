from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


class AssertionBase:
    def __init__(self, actual: T):
        self.actual = actual
        self._description: str = ""

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
