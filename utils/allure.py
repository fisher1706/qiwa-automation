import enum
from typing import Callable, Any

import allure


class TestmoProject(enum.Enum):
    CHANGE_OCCUPATION = 3
    WORK_PERMIT = 29
    VISAS = 7


def project(project_id: TestmoProject) -> Callable:
    def testcase(case_id: int) -> Callable:
        def decorator(func: Callable) -> Callable:
            @allure.testcase(
                f"https://qiwa.testmo.net/repositories/{project_id.value}?group_id={case_id}",
                "Testmo test case",
            )
            def wrapper(*args: Any, **kwargs: Any) -> Callable:
                return func(*args, **kwargs)

            return wrapper

        return decorator

    return testcase
