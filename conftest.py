from typing import Union

import pytest
from _pytest.config import Config
from _pytest.main import Session
from _pytest.reports import CollectReport, TestReport

from utils.discord_report import TestReportManager


def pytest_addoption(parser):
    parser.addoption(
        "--discord_channel", action="store", default=False, help="discord notification channel"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_report_teststatus(report: Union[CollectReport, TestReport], config: Config) -> None:
    yield
    if report.when == "setup" and report.passed is True:
        config.setup_duration = report.duration
    if report.when == "call" or report.passed is False:
        discord = config.getoption("--discord_channel")
        if discord:
            test_report = TestReportManager()
            test_report.suite_name = discord
            test_report.define_webhook_url()
            test_report.create_message_add_to_report(report, config)


def pytest_sessionfinish(session: Session, exitstatus: int):  # pylint: disable=unused-argument
    test_report = TestReportManager()
    if test_report.webhook_url:
        test_report.send_report()
        test_report.send_duration_report()
        test_report.send_count_report()
