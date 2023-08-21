from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Callable, TypeVar

import allure

from utils.assertion.assertion_base import AssertionBase
from utils.assertion.assertion_types import AssertionTypes

T = TypeVar("T")


class AssertionMixin(AssertionBase):
    def __assert(self, expected: T, method: AssertionTypes) -> None:
        operator, context = method.value
        step_name = f'Assert that {self._description} {context} "{expected}"'
        with allure.step(step_name):
            template = self._error_template(expected, context)
            assert operator(self.actual, expected), template

    def has(self, key: T) -> Callable:
        is_dict = isinstance(self.actual, Mapping)

        def _wrapper(val: Any) -> AssertionMixin:
            actual = self.actual[key] if is_dict else getattr(self.actual, key)
            self.__class__(actual).as_(
                f'"{self._description} {key}"' if self._description else f'"{key}"'
            ).equals_to(val)
            return self

        return _wrapper

    def equals_to(self, expected: T) -> None:
        self.__assert(expected, AssertionTypes.EQUAL)

    def not_equals_to(self, expected: T) -> None:
        self.__assert(expected, AssertionTypes.NOT_EQUAL)

    def in_(self, expected: T) -> None:
        self.__assert(expected, AssertionTypes.IN_)

    def is_length(self, length: int) -> None:
        if not hasattr(self.actual, "__len__"):
            raise NotImplementedError(
                f'The expected value "{self.actual}" {type(self.actual)} has no length attribute'
            )
        self.__assert(length, AssertionTypes.LENGTH)
