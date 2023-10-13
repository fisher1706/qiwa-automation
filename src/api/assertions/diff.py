import json
from typing import Any

import allure
from deepdiff import DeepDiff


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
    if difference:
        allure.attach(
            json.dumps(difference, indent=2, ensure_ascii=False, cls=SetEncoder),
            "Difference",
            allure.attachment_type.JSON,
        )
        raise AssertionError(difference)
