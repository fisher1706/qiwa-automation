from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import config


class DBClient:
    def __init__(self, db_url: str):
        self.db_url = db_url

    def set_db_session(self) -> Session:
        engine = create_engine(url=self.db_url)
        Session = sessionmaker(bind=engine)  # pylint: disable=C0103, W0621
        session = Session()
        return session

    def close_sb_session(self):
        self.set_db_session().close_all()


if __name__ == "__main__":
    db_client = DBClient(db_url=config.settings.sso_auth_db_url)
    print(db_client.set_db_session())
