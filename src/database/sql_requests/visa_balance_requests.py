import config
from data.visa.constants import BALANCE_REQUESTS_SUBMIT_FAILED_STATUS, VisaUser
from src.database.client.db_client import DBClient
from src.database.models.visa_tables import BalanceRequests


class VisaBalanceRequests:
    session = DBClient(db_url=config.settings.visa_db_url).set_db_session

    def get_balance_request_reference_number(self):
        record = (
            self.session.query(BalanceRequests)
            .filter(BalanceRequests.company_id == VisaUser.COMPANY_ID)
            .first()
        )
        return record.reference_number

    def set_balance_request_to_submit_failed(self, ref_number: str) -> None:
        record = (
            self.session.query(BalanceRequests)
            .filter(BalanceRequests.reference_number == ref_number)
            .first()
        )
        record.status = BALANCE_REQUESTS_SUBMIT_FAILED_STATUS
        self.session.commit()

    def remove_balance_request_records(self) -> None:
        records = (
            self.session.query(BalanceRequests)
            .filter(BalanceRequests.company_id == VisaUser.COMPANY_ID)
            .all()
        )
        for record in records:
            self.session.delete(record)
            self.session.commit()
