import pytest

from data.mock_mlsd.establishment import Establishment


@pytest.fixture(scope="package")
def establishment() -> Establishment:
    return Establishment(
        personal_number="1154466872",
        labor_office_id="14",
        sequence_number="2274480",
    )
