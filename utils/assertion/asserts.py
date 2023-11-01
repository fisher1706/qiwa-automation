import json
from typing import Any, TypeVar

import allure
from deepdiff import DeepDiff

from utils.assertion.assertion_mixin import AssertionMixin

T = TypeVar("T")


def assert_that(actual: T) -> AssertionMixin:
    assertion = AssertionMixin(actual=actual)
    return assertion


def assert_status_code(code: int) -> AssertionMixin:
    assertion = AssertionMixin(actual=code)
    return assertion.as_("status code")


@allure.step
def assert_data(*, expected: Any, actual: Any) -> None:
    difference = DeepDiff(expected, actual)

    allure.attach(
        json.dumps(expected, indent=2, ensure_ascii=False, default=str),
        "Expected",
        allure.attachment_type.JSON,
    )
    allure.attach(
        json.dumps(actual, indent=2, ensure_ascii=False, default=str),
        "Actual",
        allure.attachment_type.JSON,
    )
    if "values_changed" in difference.keys():
        allure.attach(
            json.dumps(difference["values_changed"], indent=2, ensure_ascii=False, default=str),
            "Difference",
            allure.attachment_type.JSON,
        )
        raise AssertionError(difference["values_changed"])
