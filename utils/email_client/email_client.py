import base64
import json
import re
import time
import traceback
from urllib.parse import parse_qs, urlparse

from utils.email_client.email_support import EmailSupport
from utils.logger import yaml_logger

logger = yaml_logger.setup_logging(__name__)


class EmailClient(EmailSupport):
    def __init__(self):
        super().__init__()
        self._confirmation_url = None
        self._confirmation_token = None

    @property
    def confirmation_url(self):
        return self._confirmation_url

    @property
    def confirmation_token(self):
        return self._confirmation_token

    def find_email_by_recipient(
        self, recipient_email, attempts=30, raise_exception=True, mark_read=True
    ):
        sleep_time = 2
        for attempt in range(attempts):
            time.sleep(sleep_time)
            logger.debug(f"Check mailbox {attempt} time(s)")
            for _ in range(3):
                try:
                    self.get_unread_email_by_recipient(
                        recipient=recipient_email, ignore_not_found=True
                    )
                    break
                except Exception:  # pylint: disable=broad-except
                    traceback.print_exc()
                    continue
            self.fetch_email_content()

            if self.email_id and mark_read:
                self.mark_email_read()
                break

        if not self.email_content:
            logger.warning(
                f"No unread emails in {attempts * sleep_time} sec. for: {recipient_email}"
            )
            if raise_exception:
                raise ValueError(f"No unread emails in {attempts * sleep_time} sec.")

    def _parse_confirmation_url(self):
        msg = str(self.email_content.body[1])
        link_pattern = re.compile(r'title([^"]*)"([^"]*)" href[^\s]+(?P<url>https([^"]*))')
        found_url = link_pattern.search(msg)
        if found_url:
            found_url = found_url.group("url")
            self._confirmation_url = found_url.replace("=\n", "").replace("3D", "")
            logger.debug(f"Email confirmation URL: {self._confirmation_url}")
        else:
            raise ValueError("Verification URL was not found in Confirmation email")

    def receive_confirmation_url(self, email_address):
        self._confirmation_url = None
        self.find_email_by_recipient(email_address)
        self._parse_confirmation_url()

    def receive_confirmation_token(self, email_address):
        self._confirmation_token = None
        self.receive_confirmation_url(email_address)
        self._get_confirmation_token()

    def _get_confirmation_token(self):
        result = urlparse(self.confirmation_url)
        if "token=" in self.confirmation_url:
            token = parse_qs(result.query)["token"][0]
        else:
            base_string = parse_qs(result.query)["p"][0]
            first_url = json.loads(json.loads(base64.b64decode(base_string + "=="))["p"])["url"]
            second = parse_qs(urlparse(first_url).query)
            token = second["token"][0]
        self._confirmation_token = token
        return token
