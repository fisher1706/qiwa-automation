from src.api.payloads.raw.delegation import GetDelegations


def get_all_delegations_request() -> dict:
    return GetDelegations().dict(exclude={"statusEn", "statusAr", "entityId", "search"})
