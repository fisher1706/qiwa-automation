from __future__ import annotations

from collections.abc import Mapping
from typing import TypeVar

from utils.assertion.assertion_base import AssertionBase
from utils.assertion.assertion_types import AssertionTypes

T = TypeVar("T")


class AssertionMixin(AssertionBase):
    def has(self, **kwargs) -> None:
        is_dict = isinstance(self.actual, Mapping)
        for key, value in kwargs.items():
            actual = self.actual[key] if is_dict else getattr(self.actual, key)
            self.as_(key).assert_(actual, value, AssertionTypes.EQUAL, "=")

    def equals_to(self, expected: T) -> AssertionMixin:
        self.assert_(self.actual, expected, AssertionTypes.EQUAL, "equals")
        return self

    def not_equals(self, expected: T) -> AssertionMixin:
        self.assert_(self.actual, expected, AssertionTypes.NOT_EQUAL, "not equals")
        return self

    def contains(self, expected: T) -> AssertionMixin:
        self.assert_(self.actual, expected, AssertionTypes.CONTAINS, "contains")
        return self

    def size_is(self, expected: int) -> AssertionMixin:
        self.assert_(len(self.actual), expected, AssertionTypes.EQUAL, "size is")
        return self

    def is_empty(self) -> AssertionMixin:
        self.assert_(len(self.actual), 0, AssertionTypes.EQUAL, "is empty")
        return self

    def is_not_empty(self) -> AssertionMixin:
        self.assert_(len(self.actual), 0, AssertionTypes.NOT_EQUAL, "is not empty")
        return self
