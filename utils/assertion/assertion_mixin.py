from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Callable, TypeVar

import allure

from utils.assertion.assertion_base import AssertionBase
from utils.assertion.assertion_types import AssertionTypes

T = TypeVar("T")


class AssertionMixin(AssertionBase):
    def _step(self, left: Any, operation: str, right: Any = "") -> Callable:
        return allure.step(f"Assert that {left} {operation} {right}")

    def has(self, **kwargs) -> None:
        is_dict = isinstance(self.actual, Mapping)
        for key, value in kwargs.items():
            actual = self.actual[key] if is_dict else getattr(self.actual, key)
            step = self._step(f"{self.description} {key}".lstrip(), "=", value)
            self.assert_(actual, value, AssertionTypes.EQUAL, step)

    def equals_to(self, expected: T) -> AssertionMixin:
        step = self._step(self.description, "equals", expected)
        self.assert_(self.actual, expected, AssertionTypes.EQUAL, step)
        return self

    def not_equals(self, expected: T) -> AssertionMixin:
        step = self._step(self.description, "not equals", expected)
        self.assert_(self.actual, expected, AssertionTypes.NOT_EQUAL, step)
        return self

    def contains(self, expected: T) -> AssertionMixin:
        step = self._step(self.description, "contains", expected)
        self.assert_(self.actual, expected, AssertionTypes.CONTAINS, step)
        return self

    def in_(self, expected: T) -> AssertionMixin:
        step = self._step(self.description, "in", expected)
        self.assert_(self.actual, expected, AssertionTypes.IN, step)
        return self

    def size_is(self, expected: int) -> AssertionMixin:
        step = self._step(self.description, "size is", expected)
        self.assert_(len(self.actual), expected, AssertionTypes.EQUAL, step)
        return self

    def is_empty(self) -> AssertionMixin:
        step = self._step(self.description, "is empty")
        self.assert_(len(self.actual), 0, AssertionTypes.EQUAL, step)
        return self

    def is_not_empty(self) -> AssertionMixin:
        step = self._step(self.description, "is not empty")
        self.assert_(len(self.actual), 0, AssertionTypes.NOT_EQUAL, step)
        return self

    def is_greater(self, expected: T) -> AssertionMixin:
        step = self._step(self.description, "greater", expected)
        self.assert_(self.actual, expected, AssertionTypes.GREATER, step)
        return self

    def is_greater_or_equal(self, expected: T) -> AssertionMixin:
        step = self._step(self.description, "greater or equal", expected)
        self.assert_(self.actual, expected, AssertionTypes.GREATER_OR_EQUAL, step)
        return self

    def is_less_or_equal(self, expected: T) -> AssertionMixin:
        step = self._step(self.description, "less or equal", expected)
        self.assert_(self.actual, expected, AssertionTypes.LESS_OR_EQUAL, step)
        return self
