from __future__ import annotations

from collections.abc import Mapping
from typing import TypeVar

from utils.assertion.assertion_base import AssertionBase
from utils.assertion.assertion_types import AssertionTypes

T = TypeVar("T")


class AssertionMixin(AssertionBase):
    def has(self, **kwargs) -> AssertionMixin:
        is_dict = isinstance(self.actual, Mapping)
        for k, v in kwargs.items():
            actual = self.actual[k] if is_dict else getattr(self.actual, k)
            self.__class__(actual).as_(
                f'"{self._description} {k}"' if self._description else f'"{k}"'
            ).equals_to(v)
        return self

    def equals_to(self, expected: T) -> AssertionMixin:
        self._assert(expected, AssertionTypes.EQUAL)
        return self

    def not_equals_to(self, expected: T) -> AssertionMixin:
        self._assert(expected, AssertionTypes.NOT_EQUAL)
        return self

    def in_(self, expected: T) -> AssertionMixin:
        self._assert(expected, AssertionTypes.IN_)
        return self

    def is_length(self, length: int) -> AssertionMixin:
        self._assert(length, AssertionTypes.LENGTH)
        return self
