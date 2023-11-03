import json
from typing import Any, Optional, TypeVar

import allure
from deepdiff import DeepDiff
from pytest_check import check

from utils.assertion.assertion_mixin import AssertionMixin

T = TypeVar("T")


def assert_that(actual: T) -> AssertionMixin:
    assertion = AssertionMixin(actual)
    assertion.assert_ = check.check_func(assertion.assert_)  # pylint: disable=no-member
    return assertion


def assert_status_code(code: int) -> AssertionMixin:
    assertion = AssertionMixin(actual=code)
    return assertion.as_("status code")


@check.check_func
def assert_data(*, expected: Any, actual: Any, title: Optional[str] = None) -> None:
    exclude = ["dictionary_item_added", "dictionary_item_removed", "attribute_added"]
    with allure.step(f"Assert {title or 'data'}"):
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
        if difference:
            for rule in exclude:
                if rule in difference.keys():
                    difference.pop(rule)

            if difference:
                allure.attach(
                    json.dumps(difference, indent=2, ensure_ascii=False, default=str),
                    "Difference",
                    allure.attachment_type.JSON,
                )
                raise AssertionError(difference)
