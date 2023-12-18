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
        self.__payment_id = None
        self.last_payment_id = None

    session = DBClient(db_url=config.settings.visa_db_url).set_db_session

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

    def get_balance_request_reference_number(self):
        record = (
            self.session.query(BalanceRequests)
            .filter(BalanceRequests.payment_id == self.last_payment_id)
            .first()
        )
        return record.reference_number

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value
        if value:
            self.last_payment_id = value
