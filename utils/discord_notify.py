# pylint: disable=import-outside-toplevel
# To execute from a commandline
def notify_to_discord(junitxml_report: str, webhook_url: str) -> None:
    def message_template(
        total: int, passed: int, failed: int, errors: int, skipped: int, duration: str
    ) -> str:
        import config

        return (
            f":earth_africa: Environment: {config.settings.env}\n"
            f":purple_circle: Total: {total}\n"
            f":green_circle: Passed: {passed}\n"
            f":red_circle: Failed: {failed}\n"
            f":orange_circle: Errors: {errors}\n"
            f":white_circle: Skipped: {skipped}\n"
            f":clock1: Duration: {duration}\n"
        )

    def parse_report(xml_report: str) -> tuple:
        import datetime
        import xml.etree.ElementTree as ET

        tree = ET.parse(xml_report)
        root = tree.getroot()[0]
        name = root.get("name")
        total = int(root.get("tests"))
        failed = int(root.get("failures"))
        errors = int(root.get("errors"))
        skipped = int(root.get("skipped"))
        passed = total - failed - errors - skipped
        time: str = root.get("time")
        duration = str(datetime.timedelta(seconds=round(float(time))))

        return name, message_template(total, passed, failed, errors, skipped, duration)

    from discord import SyncWebhook

    testsuite, message = parse_report(junitxml_report)
    SyncWebhook.from_url(webhook_url).send(message, username=testsuite)


if __name__ == "__main__":
    import sys
    from pathlib import Path

    print(len(sys.argv))

    if len(sys.argv) < 3:
        print("Usage: python discord_notify.py <junitxml report> <webhook_url>")
        sys.exit(1)

    path = Path(__file__).parent.parent
    sys.path.append(str(path))
    notify_to_discord(sys.argv[1], sys.argv[2])
