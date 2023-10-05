import allure
import pytest

from data.lo.data_set import VisitsDataSet
from src.api.app import QiwaApi


@allure.title('Book & Cancel visits')
@pytest.mark.parametrize(
    'test_data',
    VisitsDataSet.visits_api_test_data,
    ids=[_['description'] for _ in VisitsDataSet.visits_api_test_data]
)
def test_book_visits(test_data):
    qiwa = QiwaApi.login_as_user(test_data['user_id'])
    qiwa.visits_api_actions.cancel_active_visit(test_data['user_id'])
    qiwa.visits_api_actions.book_visit(**test_data['booking_data'])
    qiwa.visits_api_actions.cancel_active_visit(test_data['user_id'])


@allure.title('Edit visits')
@pytest.mark.parametrize(
    'test_data',
    VisitsDataSet.visits_api_edit_test_data,
    ids=[_['description'] for _ in VisitsDataSet.visits_api_edit_test_data]
)
def test_edit_visits(test_data):
    qiwa = QiwaApi.login_as_user(test_data['user_id'])
    qiwa.visits_api_actions.cancel_active_visit(test_data['user_id'])
    qiwa.visits_api_actions.book_visit(**test_data['booking_data'])
    qiwa.visits_api_actions.edit_visit(user_id=test_data['user_id'], **test_data['booking_data_edit'])
    qiwa.visits_api_actions.cancel_active_visit(test_data['user_id'])
