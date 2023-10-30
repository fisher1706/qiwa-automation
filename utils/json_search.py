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
def search_data_by_attribute(data: Root, **attribute) -> Any:
    x = list(attribute.items())
    expression = f'data[?attributes."{x[0][0]}" == \'{x[0][1]}\']'
    return search_by_data(expression, data=data.dict(exclude_unset=True))
