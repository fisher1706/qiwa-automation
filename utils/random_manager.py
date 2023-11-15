import random
import secrets
import string
from random import choices, randint

import config


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

    def random_phone_number(self, size: int = 9, prefix: str = "966") -> str:
        return f"{prefix}{self._random_int(size)}"

    @classmethod
    def random_eng_string(cls, letters_quantity: int) -> str:
        return "".join(
            random.choice(string.ascii_lowercase) for x in range(letters_quantity)
        ).lower()

    @classmethod
    def random_ar_string(cls, letters_quantity):
        ar_string = "شسزرذدخحجثتباءيوهنملكقفغعظطضصىئؤةإأٱآ"
        return "".join(random.choice(ar_string) for x in range(letters_quantity)).lower()

    @staticmethod
    def generate_safe_url_string(str_len: int = 10) -> str:
        return secrets.token_urlsafe(str_len)

    def generate_url(self, size: int = 8, path: str = "") -> str:
        return f"https://{'auto'}-{self.random_alphanumeric(size)}-{config.qiwa_urls.auth}{path}"
