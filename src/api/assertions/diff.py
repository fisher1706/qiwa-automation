import allure
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
