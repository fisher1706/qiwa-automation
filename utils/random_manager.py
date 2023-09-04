import random
import secrets
import string
from random import choice, choices, randint

from data.constants import UserType


class RandomManager:
    @staticmethod
    def _random_int(size):
        range_start = 10 ** (size - 1)
        range_end = (10**size) - 1
        return randint(range_start, range_end)

    @staticmethod
    def random_string(size):
        return "".join(choices(string.ascii_letters, k=size))

    @staticmethod
    def random_alphanumeric(size):
        return "".join(choices(string.ascii_letters + string.digits, k=size))

    def random_email(self, personal_number=None, domain="qa.qiwa.tech", prefix="auto"):
        if not personal_number:
            personal_number = self.random_alphanumeric(8).lower()
        email = f"{prefix}+{personal_number}@{domain}"
        return email

    def random_nid(self, user_type, valid_phone=True):
        first_char = {UserType.SAUDI: 1, UserType.EXPAT: 2, UserType.BORDER: choice(range(3, 6))}
        random_number = self._random_int(8)
        prefix = first_char.get(user_type)
        if valid_phone:
            suffix = choice(range(0, 8))
        else:
            suffix = choice(range(8, 10))
        return f"{prefix}{random_number}{suffix}"

    def random_phone_number(self, size: int = 9, prefix: str = "966") -> str:
        return f"{prefix}{self._random_int(size)}"

    @staticmethod
    def select_random_element_from_list(start_element, stop_element):
        return random.randrange(start_element, stop_element - 1)

    @classmethod
    def random_eng_string(cls, letters_quantity):
        return "".join(
            random.choice(string.ascii_lowercase) for x in range(letters_quantity)
        ).lower()

    @classmethod
    def random_ar_string(cls, letters_quantity):
        ar_string = "شسزرذدخحجثتباءيوهنملكقفغعظطضصىئؤةإأٱآ"
        return "".join(random.choice(ar_string) for x in range(letters_quantity)).lower()

    @staticmethod
    def set_of_random_privileges(
        number_of_privileges=27, skipped_privilege=12, privileges_in_set=6
    ):
        privileges = random.choices(
            [x for x in range(number_of_privileges) if x != skipped_privilege], k=privileges_in_set
        )
        return privileges

    @staticmethod
    def generate_safe_url_string(str_len=10):
        return secrets.token_urlsafe(str_len)

    def generate_url(self, size=8, prefix="auto", host="auth.qiwa.tech", path=None):
        _path = f"/{path}" if path else ""
        return f"https://{prefix}-{self.random_alphanumeric(size)}-{host}{_path}"
