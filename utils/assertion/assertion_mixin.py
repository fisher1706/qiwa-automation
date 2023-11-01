from __future__ import annotations

from collections.abc import Mapping
from typing import TypeVar

import allure
from pytest_check import check

from utils.assertion.assertion_base import AssertionBase
from utils.assertion.assertion_types import AssertionTypes

T = TypeVar("T")


class AssertionMixin(AssertionBase):
    @check.check_func
    def __assert(self, expected: T, method: AssertionTypes) -> AssertionMixin:
        operator, context = method.value
        step_name = f'Assert that {self._description} {context} "{expected}"'
        with allure.step(step_name):
            template = self._error_template(expected, context)
            assert operator(self.actual, expected), template
            return self

    def has(self, **kwargs) -> AssertionMixin:
        is_dict = isinstance(self.actual, Mapping)
        for k, v in kwargs.items():
            actual = self.actual[k] if is_dict else getattr(self.actual, k)
            self.__class__(actual).as_(
                f'"{self._description} {k}"' if self._description else f'"{k}"'
            ).equals_to(v)
        return self

    def equals_to(self, expected: T) -> AssertionMixin:
        return self.__assert(expected, AssertionTypes.EQUAL)

    def not_equals_to(self, expected: T) -> AssertionMixin:
        return self.__assert(expected, AssertionTypes.NOT_EQUAL)

    def in_(self, expected: T) -> AssertionMixin:
        return self.__assert(expected, AssertionTypes.IN_)

    def is_length(self, length: int) -> AssertionMixin:
        if not hasattr(self.actual, "__len__"):
            raise NotImplementedError(
                f'The expected value "{self.actual}" {type(self.actual)} has no length attribute'
            )
        return self.__assert(length, AssertionTypes.LENGTH)
