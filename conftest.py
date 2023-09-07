import _pytest.terminal
from _pytest.main import Session
from discord import SyncWebhook

import config
from utils.discord_report import DISCORD_HOOKS


def pytest_addoption(parser):
    parser.addoption(
        "--discord_channel", action="store", default=False, help="discord notification channel"
    )


def pytest_sessionfinish(session: Session, exitstatus: int):  # pylint: disable=unused-argument
    discord = session.config.getoption("--discord_channel")
    if discord:
        reporter: _pytest.terminal.TerminalReporter = session.config.pluginmanager.get_plugin(
            "terminalreporter"
        )
        stats = reporter.stats
        passed = len(stats.get("passed", []))
        failed = len(stats.get("failed", []))
        errors = len(stats.get("error", []))
        skipped = len(stats.get("skipped", []))
        total = passed + failed + errors + skipped
        message = (
            f":blue_circle: Environment: {config.settings.env}\n"
            f":purple_circle: Total: {total}\n"
            f":green_circle: Passed: {passed}\n"
            f":red_circle: Failed: {failed}\n"
            f":orange_circle: Errors: {errors}\n"
            f":white_circle: Skipped: {skipped}\n"
        )
        webhook_url = DISCORD_HOOKS[discord]
        SyncWebhook.from_url(webhook_url).send(message, username=discord)
