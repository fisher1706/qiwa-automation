import email
import imaplib
import socket

from data.constants import EmailConst
from utils.logger import yaml_logger
from src.api.models.model_builder import ModelBuilder

logger = yaml_logger.setup_logging(__name__)

MAIL_LOGIN = "qiwaqa@p2h.com"
MAIL_PASS = "evevTSbfuZJ7B5"


class EmailSupport:
    def __init__(self):
        self.email_content = None
        self.imap_session = None
        self.init_imap_session(EmailConst.IMAP_DOMAIN)
        self.email_id = None

    def init_imap_session(self, imap_domain):
        """
        Init IMAP session for provided domain
        """
        try:
            self.imap_session = imaplib.IMAP4_SSL(imap_domain)
            typ, _ = self.imap_session.login(MAIL_LOGIN, MAIL_PASS)
            logger.info("IMAP session successfully created")
            if typ != EmailConst.STATUS_OK:
                raise EnvironmentError("Not able to sign in to mailbox!")
        except socket.gaierror:
            self.imap_session = None
        except Exception as e:  # pylint: disable=broad-except
            logger.error("IMAP session creation failed")
            logger.error(e)

    def get_unread_emails(self):
        id_list = None
        if self.imap_session:
            self.imap_session.select(EmailConst.INBOX_FOLDER, readonly=True)

            typ, data = self.imap_session.search(None, f"({EmailConst.UNSEEN_EMAILS})")
            if typ != EmailConst.STATUS_OK:
                raise FileNotFoundError("Requester Inbox folder was not found in the mailbox")

            unread_ids = data[0]
            id_list = unread_ids.split()

        return id_list

    def get_unread_email_by_recipient(self, recipient, ignore_not_found=False):
        self.email_id = None
        if not self.imap_session:
            raise AttributeError("IMAP session was not initiated")

        self.imap_session.select(EmailConst.INBOX_FOLDER, readonly=True)
        typ, data = self.imap_session.search(
            None, f'(TO "{recipient}" {EmailConst.UNSEEN_EMAILS})'
        )
        if typ == EmailConst.STATUS_OK:
            attempt_number = 0
            while attempt_number <= 3:
                typ, data = self.imap_session.search(
                    None, f'(TO "{recipient}" {EmailConst.UNSEEN_EMAILS})'
                )
                if len(data[0].split()) > 0:
                    self.email_id = sorted(data[0].split())[-1]
                    break
                if attempt_number == 3:
                    self.email_id = data[0]
                    break
                self.imap_session.select(EmailConst.INBOX_FOLDER, readonly=True)
                typ, data = self.imap_session.search(
                    None, f'(TO "{recipient}" {EmailConst.UNSEEN_EMAILS})'
                )
                attempt_number += 1
        else:
            raise FileNotFoundError("Requester Inbox folder was not found in the mailbox")

        if len(data[0]) == 0:
            self.email_id = None

            if not ignore_not_found:
                raise FileNotFoundError(
                    f"No unread emails were found in the mailbox for {recipient}"
                )
        return self

    def fetch_email_content(self):
        self.email_content = None
        if self.email_id:
            _, data = self.imap_session.fetch(self.email_id, EmailConst.EMAIL_FORMAT)
            email_body = data[0][1]
            mail = email.message_from_bytes(email_body)
            self.email_content = ModelBuilder.build_email(mail)

    def mark_email_read(self):
        self.imap_session.select(EmailConst.INBOX_FOLDER, readonly=False)
        self.imap_session.store(self.email_id, EmailConst.ADD_FLAG, EmailConst.FLAG_SEEN)
        self.imap_session.select(EmailConst.INBOX_FOLDER, readonly=True)

    def logout_imap_session(self):
        if self.imap_session.state is EmailConst.IMAP_SESSION_ACTIVE:
            self.imap_session.close()
            self.imap_session.logout()
            logger.info("IMAP session session deactivated")
        else:
            logger.info("Reject IMAP session deactivation")
