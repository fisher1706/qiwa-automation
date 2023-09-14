from traceback import format_stack
from typing import Union

from pytest_check import check
from selene import Collection, be, have, query

from utils.logger import yaml_logger

logger = yaml_logger.setup_logging(__name__)


def soft_assert(condition, error_message=""):
    with check:
        assert condition, error_message + "\r\n" + "".join(format_stack(limit=15))


def soft_assert_text(element, text="", element_name=None, expected=True, timeout=0):
    error_message = (
        f"Element {element_name if element_name else str(element)} "
        f"should {'not' if not expected else ''} have text {text} "
    )
    condition = be.visible if expected else be.hidden
    element.with_(timeout=timeout).wait_until(condition)
    if element.wait_until(be.visible) and expected:
        has_text = element.with_(timeout=timeout).wait_until(have.text(str(text)))
        soft_assert(has_text == expected, error_message + f"Actual: {element.get(query.text)}")
    else:
        soft_assert(not expected, error_message + "Actual: element is hidden")


def soft_assert_list(elements: Union[list, Collection], expected_text: list):
    expected_quantity = len(expected_text)
    if isinstance(elements, list):
        actual_quantity_match = len(elements)
    else:
        actual_quantity_match = elements.with_(timeout=2).wait_until(have.size(expected_quantity))
    soft_assert(
        actual_quantity_match,
        "Steps quantity is not what expected. "
        f"Expected: {expected_quantity}. "
        f"Actual: {len(elements)}",
    )
    if not actual_quantity_match:
        for num, element in enumerate(elements, start=1):
            logger.warning(
                str(num) + '. Element: "' + str(element) + '" text: "' + element.get(query.text)
            )
    if actual_quantity_match:
        for element, text in zip(elements, expected_text):
            soft_assert_text(element, text, element_name=text)
