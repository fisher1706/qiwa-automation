import re

from selene.api import Condition, Element, ElementCondition, query


def have_in_text_number(number) -> Condition[Element]:
    def condition(element: Element) -> None:
        text = element.get(query.text)
        parsed_number = __parse_number_from_text(text)
        if parsed_number == "" or float(parsed_number) != number:
            raise AssertionError(
                f"expected number was: {number} "
                f"actual text was: {text} "
                f"with parsed int number: {parsed_number}"
            )

    return ElementCondition(f"has in text the int number: {number}", condition)


def have_any_number() -> Condition[Element]:
    def condition(element: Element) -> None:
        text = element.get(query.text)
        parsed_number = __parse_number_from_text(text)
        if parsed_number == "":
            raise AssertionError(f"no number found in text: {text} ")

    return ElementCondition("has a number in text", condition)


def __parse_number_from_text(text) -> str:
    return re.sub(r"[^0-9.]", "", text)
