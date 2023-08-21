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
    day: str = "01"
    month: str = "01"
    year: str = "1430"

    def __post_init__(self):
        if not self.email:
            self.email = RandomManager().random_email(self.personal_number)
