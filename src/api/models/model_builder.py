from data.constants import Language
from helpers.logger import yaml_logger
from helpers.random_manager import RandomManager
from src.api.models.account import Account
from src.api.models.email import Email

logger = yaml_logger.setup_logging(__name__)


class ModelBuilder:
    @staticmethod
    def build_random_account(
        personal_number, password, email=None, phone_number=None, code="0000"
    ):
        if not email:
            email = RandomManager().random_email(personal_number=personal_number)
        if not phone_number:
            phone_number = RandomManager().random_phone_number()
        logger.info(f"New National ID: {personal_number}, Email: {email}")
        return Account(
            personal_number=personal_number,
            email=email,
            password=password,
            phone_number=phone_number,
            confirmation_code=code,
            language=Language.EN,
            day="01",
            month="01",
            year="1430",
        )

    @staticmethod
    def build_email(mail):
        return Email(
            _from=mail["from"],
            _to=mail["to"],
            date=mail["date"],
            subject=mail["subject"],
            body=mail.get_payload(),
        )
