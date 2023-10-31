import json
from typing import Any

import allure
import jmespath

from src.api.models.qiwa.raw.root import Root


def search_in_json(key, json_response):
    result = jmespath.search(key, json_response)[0]
    return result


@allure.step
def search_by_data(expression: str, data: Any) -> Any:
    result = jmespath.search(expression, data)
    allure.attach(
        json.dumps(result, indent=2, ensure_ascii=False, default=str) if result else "None",
        "Search result",
        allure.attachment_type.JSON,
    )
    return result


@allure.step
def search_data_by_attributes(data: Root, **attributes) -> Any:
    attrs = [
        f"attributes.\"{key}\" == '{attributes[key]}'"
        if not isinstance(attributes[key], int)
        else f'attributes."{key}" == `{attributes[key]}`'
        for key in attributes
    ]
    expression = f"data[? {' && '.join(attrs)}]"
    return search_by_data(expression, data=data.dict(exclude_unset=True))
