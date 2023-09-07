import _pytest.terminal
from _pytest.main import Session
from discord import SyncWebhook

import config


def pytest_addoption(parser):
    parser.addoption(
        "--discord_channel", action="store", default=False, help="discord notification channel"
    )


def pytest_sessionfinish(session: Session, exitstatus: int):  # pylint: disable=unused-argument
    discord_webhook = session.config.getoption("--discord_channel")
    if discord_webhook:
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
            f":earth_africa: Environment: {config.settings.env}\n"
            f":purple_circle: Total: {total}\n"
            f":green_circle: Passed: {passed}\n"
            f":red_circle: Failed: {failed}\n"
            f":orange_circle: Errors: {errors}\n"
            f":white_circle: Skipped: {skipped}\n"
        )
        SyncWebhook.from_url(discord_webhook).send(message, username="Test Run")
