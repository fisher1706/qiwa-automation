import json
from typing import Any

import allure
import jmespath


def search_in_json(key, json_response):
    result = jmespath.search(key, json_response)[0]
    return result


@allure.step
def search_by_data(expression: str, data: dict) -> Any:
    result = jmespath.search(expression, data)
    if result:
        allure.attach(
            json.dumps(result, indent=2, ensure_ascii=False),
            "RESULT",
            allure.attachment_type.JSON,
        )
    else:
        allure.attach(
            result,
            "RESULT",
            allure.attachment_type.TEXT,
        )
    return result
