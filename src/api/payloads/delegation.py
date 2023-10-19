from data.delegation import general_data
from src.api.payloads.raw.delegation import (
    ChangeRequestStatus,
    CreateDelegation,
    GetDelegations,
    ResendDelegationRequest,
)


def get_all_delegations_request() -> dict:
    return GetDelegations().dict(exclude={"statusEn", "statusAr", "entityId", "search"})


def filter_delegations_by_status_request(status_en: str) -> dict:
    return GetDelegations(statusEn=status_en).dict(exclude={"statusAr", "entityId", "search"})


def create_new_delegation(employee_nid: str, duration: int) -> dict:
    return CreateDelegation(employeeNid=employee_nid, durationMonth=duration).dict()


def reject_delegation_request() -> dict:
    return ChangeRequestStatus(
        status=general_data.REJECTED, rejectReason=general_data.REJECT_REASON
    ).dict()


def resend_delegation_request(delegation_id: int) -> dict:
    return ResendDelegationRequest(id=delegation_id).dict()
