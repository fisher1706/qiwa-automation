from sqlalchemy import and_

import config
from data.visa.constants import (
    BALANCE_REQUESTS_SUBMIT_FAILED_STATUS,
    BALANCE_REQUESTS_WAITING_STATUS,
)
from src.database.client.db_client import DBClient
from src.database.models.visa_tables import BalanceRequests


class VisaBalanceRequests:
    def __init__(self):
        self.payment_id = None

    session = DBClient(db_url=config.settings.visa_db_url).set_db_session()

    def remove_blocking_status_record(self):
        statuses = [BALANCE_REQUESTS_WAITING_STATUS, BALANCE_REQUESTS_SUBMIT_FAILED_STATUS]
        if self.payment_id:
            record = self.session.query(BalanceRequests).filter(
                and_(BalanceRequests.status.in_(statuses)),
                BalanceRequests.payment_id == self.payment_id,
            )
            if record.count() > 0:
                self.session.delete(record.one())
                self.session.commit()
