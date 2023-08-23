from dataclasses import dataclass, field

from data.constants import UserInfo
from utils.random_manager import RandomManager


@dataclass
class Account:
    personal_number: str | int
    password: str = UserInfo.PASSWORD
    email: str = ""
    phone_number: str = field(default_factory=RandomManager().random_phone_number)
    confirmation_code: str = "0000"
    language: str = "en"
    birth_day: str = "1430-01-01"

    def __post_init__(self):
        if not self.email:
            self.email = RandomManager().random_email(self.personal_number)
