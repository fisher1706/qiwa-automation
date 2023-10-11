from json import dumps

import allure
from deepdiff import DeepDiff


def assert_not_difference(entity1: dict, entity2: dict) -> None:
    difference = DeepDiff(entity1, entity2)
    if difference:
        allure.attach(
            dumps(difference.to_dict(), indent=2, ensure_ascii=False).encode("utf8").decode(),
            "DIFFERENCE",
            allure.attachment_type.JSON,
        )
        raise AssertionError(difference)
