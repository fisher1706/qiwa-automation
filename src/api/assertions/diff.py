from json import dumps
from typing import Any

import allure
import jmespath
from deepdiff import DeepDiff


@allure.step
def assert_not_difference(entity1: dict, entity2: dict) -> None:
    difference = DeepDiff(entity1, entity2)
    if difference:
        allure.attach(
            difference.pretty(),
            "DIFFERENCE",
            allure.attachment_type.TEXT,
        )
        raise AssertionError(difference)


@allure.step
def search_by_data(expression: str, data: dict) -> Any:
    result = jmespath.search(expression, data)
    allure.attach(
        dumps(result, indent=2, ensure_ascii=False),
        "RESULT",
        allure.attachment_type.JSON,
    )
    return result
