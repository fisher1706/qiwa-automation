from src.api.payloads.raw.delegation import GetDelegations


def get_all_delegations_request() -> dict:
    return GetDelegations().dict(exclude={"statusEn", "statusAr", "entityId", "search"})


def filter_delegations_by_status_request(status_en: str) -> dict:
    return GetDelegations(statusEn=status_en).dict(exclude={"statusAr", "entityId", "search"})
