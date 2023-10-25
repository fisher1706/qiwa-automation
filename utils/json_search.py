import json
from typing import Any

import allure
import jmespath


def search_in_json(key, json_response):
    result = jmespath.search(key, json_response)[0]
    return result


@allure.step
def search_by_data(expression: str, data: Any) -> Any:
    result = jmespath.search(expression, data)
    allure.attach(
        json.dumps(result, indent=2, ensure_ascii=False) if result else "None",
        "Search result",
        allure.attachment_type.JSON,
    )
    return result
