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
    class SetEncoder(json.JSONEncoder):
        def default(self, obj):
            return list(obj)

    difference = DeepDiff(expected, actual)

    allure.attach(
        json.dumps(expected, indent=2, ensure_ascii=False, cls=SetEncoder),
        "Expected",
        allure.attachment_type.JSON,
    )
    allure.attach(
        json.dumps(actual, indent=2, ensure_ascii=False, cls=SetEncoder),
        "Actual",
        allure.attachment_type.JSON,
    )
    if "values_changed" in difference.keys():
        allure.attach(
            json.dumps(difference["values_changed"], indent=2, ensure_ascii=False, cls=SetEncoder),
            "Difference",
            allure.attachment_type.JSON,
        )
        raise AssertionError(difference["values_changed"])
