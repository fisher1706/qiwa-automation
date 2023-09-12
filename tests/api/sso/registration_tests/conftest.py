import pytest

from data.sso import users_data
from src.database.actions.auth_db_actions import (
    delete_account_activities_data,
    delete_account_data_from_db,
)


@pytest.fixture
def clear_db_registration_data_saudi():
    yield
    delete_account_data_from_db(personal_number=users_data.SAUDI_NATIONAL_ID)


@pytest.fixture
def clear_db_registration_data_expat():
    yield
    delete_account_data_from_db(personal_number=users_data.EXPAT_IQAMA_ID, expat=True)


@pytest.fixture
def clear_saudi_account_activities():
    yield
    delete_account_activities_data(personal_number=users_data.SAUDI_NATIONAL_ID)


@pytest.fixture
def clear_expat_account_activities():
    yield
    delete_account_activities_data(personal_number=users_data.EXPAT_IQAMA_ID)
