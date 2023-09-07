from __future__ import annotations

import dataclasses
import os
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseSettings, HttpUrl

Envs = Literal["local", "demo", "stage"]
Domains = Literal["qiwa.tech", "qiwa.info"]


class Settings(BaseSettings):
    env: Envs
    domain: Domains
    mock_mlsd_url: Optional[HttpUrl]
    # Driver settings
    browser_name: Literal["chrome", "firefox", "opera"] = "chrome"
    timeout: int = 20
    headless: bool = False
    maximize_window: bool = True
    window_width: int = 1440
    window_height: int = 900
    hold_browser_open: bool = False
    # Selenoid settings
    remote_url: Optional[HttpUrl]
    remote_enableVNC: bool = True
    remote_enableVideo: bool = True
    remote_enableLog: bool = True
    remote_acceptInsecureCerts: bool = True

    @classmethod
    def for_env(cls, env: Optional[Envs]) -> Settings:
        """
        Factory method to init Settings with values from corresponding .env file.
        """
        env = env or "local"
        path = Path(__file__).parent
        return cls(_env_file=path.joinpath(f".env.{env}"), env=env)


@dataclasses.dataclass
class QiwaUrls:
    # pylint: disable=too-many-instance-attributes
    # Instantiate URLs
    domain: Domains

    def __post_init__(self) -> None:
        domain = self.domain
        protocol = "https://"
        self.api: str = f"{protocol}api.{domain}"
        self.spa: str = f"{protocol}spa.{domain}"
        self.auth: str = f"{protocol}auth.{domain}"
        self.user_management: str = f"{protocol}um.{domain}"
        self.self_subscription: str = f"{protocol}self-subscription.{domain}"
        self.certificates_validation: str = f"{protocol}certificates-validation.{domain}"
        self.qiwa_change_occupation: str = f"{protocol}api-change-occupation.{domain}"
        self.qiwa_ott_service: str = f"{protocol}internal-ott-service.{domain}"
        self.employee_transfer: str = f"{protocol}employee-transfer.{domain}"
        self.laborer_sso_auth_api: str = f"{protocol}laborer-sso-auth-api.{domain}"
        self.laborer_sso_auth: str = f"{protocol}laborer-sso-auth.{domain}"
        self.delegation_service: str = f"{protocol}delegationservice.{domain}"
        self.delegation_service_api: str = f"{protocol}api-proxy.{domain}"
        self.contract_management: str = f"{protocol}contract-management.{domain}"
        self.internal_payment: str = f"{protocol}internal-payment.{domain}"


settings = Settings.for_env(os.getenv("ENV"))
qiwa_urls = QiwaUrls(settings.domain)

if __name__ == "__main__":
    # To check the actual config values on start,
    # simply running `python config.py`
    print(repr(settings))
    print(repr(qiwa_urls))
