from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import config


class DBClient:
    # __db_instance = None
    #
    # def __new__(cls):
    #     if cls.__db_instance is None:
    #         cls.__db_instance = super().__new__(cls)
    #     return cls.__db_instance
    #
    def __del__(self):
        DBClient().close_session()

    def __init__(self):
        self.sso_auth_db_url = config.settings.sso_auth_db_url

    def set_auth_db_session(self) -> Session:
        engine = create_engine(url=self.sso_auth_db_url)
        Session = sessionmaker(bind=engine)  # pylint: disable=C0103, W0621
        session = Session()
        return session

    def close_session(self) -> None:
        self.set_auth_db_session().close()


if __name__ == "__main__":
    db_client = DBClient()
    print(db_client.set_auth_db_session())
