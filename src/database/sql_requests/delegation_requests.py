import config
from src.database.client.db_client import DBClient
from src.database.models.delegation_tables import (
    DelegationApproveRequests,
    DelegationSms,
)


class DelegationRequests:
    session = DBClient(db_url=config.settings.delegation_db_url).set_db_session()

    def get_sms_request(self, phone_number: str):
        sms_data = (
            self.session.query(DelegationSms)
            .filter(DelegationSms.phone_number == phone_number)
            .order_by(DelegationSms.created_at.desc())
            .first()
        )
        return sms_data.sms_text

    def get_delegation_request(self, delegation_id: int, status: str):
        delegation_request = (
            self.session.query(DelegationApproveRequests)
            .filter(DelegationApproveRequests.delegation_id.like(delegation_id))
            .filter(DelegationApproveRequests.status.like(status))
            .order_by(DelegationApproveRequests.created_at.desc())
            .first()
        )
        self.session.commit()
        return delegation_request
