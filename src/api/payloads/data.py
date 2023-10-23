from typing import Any


def data(data_type: Any, attributes: Any) -> dict:
    return {"data": {"type": data_type, "attributes": attributes}}


def change_occupation(attributes: Any) -> dict:
    return data("change-occupation", attributes)


def group(attributes: Any) -> dict:
    return data("group", attributes)
