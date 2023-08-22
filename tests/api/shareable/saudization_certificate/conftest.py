import pytest

from data.mock_mlsd.establishment import Establishment
from src.api.constants import nitaq


@pytest.fixture
def create_green_nitaq_establishment(parametrized_owner):
    return parametrized_owner()


@pytest.fixture
def green_nitaq_establishment() -> Establishment:
    establishment = Establishment(
        labor_office_id="14",
        sequence_number="2274480",
        personal_number="1154466872",
        nitaq_color_id=nitaq.ColorID.GREEN,
        nitaq_color_name=nitaq.ColorName.GREEN,
        nitaq_color_code=nitaq.ColorCode.GREEN,
    )
    return establishment


@pytest.fixture
def red_nitaq_establishment() -> Establishment:
    establishment = Establishment(
        labor_office_id="18",
        sequence_number="2274358",
        personal_number="1585718118",
        nitaq_color_id=nitaq.ColorID.RED,
        nitaq_color_name=nitaq.ColorName.RED,
        nitaq_color_code=nitaq.ColorCode.RED,
    )
    return establishment


@pytest.fixture
def no_certificate_establishment() -> Establishment:
    establishment = Establishment(
        labor_office_id="41",
        sequence_number="2287492",
        personal_number="1377602666",
    )
    return establishment
