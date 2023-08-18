from src.api.payloads.data import change_occupation
from src.api.payloads.raw.change_occupation import CreateRequest, Laborer


def create_change_occupation_request(
    labor_office_id: str, sequence_number: str, *laborers: Laborer
) -> dict:
    request = CreateRequest(
        labor_office_id=labor_office_id, sequence_number=sequence_number, laborers=[*laborers]
    )
    return change_occupation(request).dict()
