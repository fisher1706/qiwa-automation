from __future__ import annotations

import os
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseSettings, HttpUrl, RedisDsn

Envs = Literal["local", "demo", "stage"]


class Settings(BaseSettings):
    project_env: str

    env_url: HttpUrl
    api_url: HttpUrl
    mock_mlsd_url: HttpUrl
    mock_nic_url: HttpUrl
    mock_unifonic_url: HttpUrl
    internal_payment: HttpUrl
    elastic_url: HttpUrl
    laborer_sso_api_url: HttpUrl
    laborer_sso_ui_url: HttpUrl
    redis_url: RedisDsn
    allure_url: HttpUrl
    contract_management: HttpUrl

    # Stage URLs
    employee_transfer: Optional[HttpUrl]
    um_ibm_test: Optional[HttpUrl]
    ibm_url: Optional[HttpUrl]
    payment_gateway_url: Optional[HttpUrl]

    # Qiwa URLs
    # TODO: make domain based
    qiwa_spa_url: HttpUrl
    qiwa_um_url: HttpUrl
    qiwa_self_subscription_url: HttpUrl
    qiwa_certificates_validation_url: HttpUrl
    qiwa_change_occupation_url: HttpUrl
    qiwa_ott_service_url: HttpUrl
    qiwa_delegation_url: HttpUrl

    # Driver settings
    browser_name: Literal["chrome", "firefox", "opera"] = "chrome"
    timeout: int = 20
    headless: bool = False
    maximize_window: bool = True
    window_width: int = 1440
    window_height: int = 900
    hold_browser_open: bool = False
    remote_url: Optional[HttpUrl] = None
    remote_enableVNC: bool = True
    remote_enableVideo: bool = True
    remote_enableLog: bool = True
    remote_acceptInsecureCerts: bool = True

    @classmethod
    def for_env(cls, env: Optional[Envs] = None) -> Settings:
        """
        Factory method to init Settings with values from corresponding .env file.
        Demo settings are used as default, but if .env.local is present (so tests run locally),
        any value in it will override corresponding setting from demo,
        the same is for explicitly passed environment to `Settings.for_env(...)` method (for stage purposes).
        """
        kwargs: dict = {}
        envs_order = ["demo"]
        path = Path(__file__).parent
        if env:
            envs_order.append(env)
        elif os.path.isfile(path.joinpath(".env.local")):
            envs_order.append("local")
            # As demo settings are default, in case of local run
            # we need to pass remote_url=None explicitly, to avoid overriding it in .env.local
            kwargs["remote_url"] = None
        env_files = [path.joinpath(f".env.{env}") for env in envs_order]
        return cls(_env_file=env_files, **kwargs)


settings = Settings.for_env(os.getenv("ENV"))

if __name__ == "__main__":
    # To check the actual config values on start,
    # simply running `python config.py`
    print(repr(settings))
