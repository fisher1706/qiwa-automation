import enum
import functools
import types
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
    EMPLOYEE_LIST = 11
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


def allure_steps(cls):
    for attr in cls.__dict__:
        if isinstance(getattr(cls, attr), types.FunctionType) and not attr.startswith("_"):
            setattr(cls, attr, allure.step(getattr(cls, attr)))
    return cls
