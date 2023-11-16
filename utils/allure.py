import enum
import functools
from typing import Any, Callable

import allure
from allure_commons.types import LinkType


class TestmoProject(enum.Enum):
    __test__ = False
    LMI = 15
    CHANGE_OCCUPATION = 3
    CONTRACT_MANAGEMENT = 4
    VISAS = 7
    DELEGATION = 9
    EMPLOYEE_TRANSFER = 10
    LABOR_OFFICE = 16
    USER_MANAGEMENT = 26
    WORK_PERMIT = 29
    QIWA_SSO = 23
    INDIVIDUALS = 21


def project(project_id: TestmoProject) -> Callable:
    def testcase(*case_ids: int) -> Callable:
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Callable:
                for case_id in case_ids:
                    allure.dynamic.link(
                        f"https://qiwa.testmo.net/repositories/{project_id.value}?case_id={case_id}",
                        LinkType.TEST_CASE,
                        f"Testmo test case ({case_id})",
                    )
                return func(*args, **kwargs)

            return wrapper

        return decorator

    return testcase


def add_allure_step_for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)) and not attr.startswith("_"):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate
