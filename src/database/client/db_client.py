from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class DBClient:
    def __init__(self, db_url: str):
        self._db_url = db_url

    def __del__(self):
        self.close_db_session()

    @property
    def set_db_session(self):
        try:
            engine = create_engine(url=self._db_url)
            Session = sessionmaker(bind=engine)  # pylint: disable=C0103, W0621
            session = Session()
            return session
        except AttributeError:
            return None

    def close_db_session(self):
        # should be always called in the end of the session
        self.set_db_session.close()
