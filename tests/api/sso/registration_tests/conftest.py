import pytest

from data.sso import users_data_constants as users_data
from src.database.actions.auth_db_actions import (
    delete_account_activities_data,
    delete_account_data_from_db,
)


@pytest.fixture
def clear_saudi_db_registration_data():
    yield
    delete_account_data_from_db(personal_number=users_data.SAUDI_FOR_SIGN_UP)


@pytest.fixture
def clear_expat_db_registration_data():
    yield
    delete_account_data_from_db(personal_number=users_data.EXPAT_FOR_SIGN_UP)


@pytest.fixture
def clear_saudi_account_activities():
    yield
    delete_account_activities_data(personal_number=users_data.SAUDI_FOR_SIGN_UP)


@pytest.fixture
def clear_expat_account_activities():
    yield
    delete_account_activities_data(personal_number=users_data.EXPAT_FOR_SIGN_UP)
