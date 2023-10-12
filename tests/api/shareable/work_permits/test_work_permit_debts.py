from http import HTTPStatus

import pytest

from src.api.assertions.model import validate_model
from src.api.models.qiwa.work_permit import work_permit_debts
from utils.assertion import assert_status_code, assert_that


@pytest.mark.parametrize("page, per_page", [(1, 10), (2, 7), (3, 11)])
def test_get_work_permit_debts_info(api, page, per_page):
    response = api.wp_debts_api.get_info(page, per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = validate_model(response.json(), work_permit_debts)
    assert_that(json.data).as_("data").is_length(per_page)
    assert_that(json.meta.total_count).as_("total_count").equals_to(300)
    assert_that(json.meta.all_paid).as_("all_paid").equals_to(False)


def test_get_work_permit_debts_info_with_per_page_more_than_total(api):
    total = 300
    response = api.wp_debts_api.get_info(per=301)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = validate_model(response.json(), work_permit_debts)
    assert_that(json.data).as_("data").is_length(total)
    assert_that(json.meta.total_count).as_("total_count").equals_to(total)
    assert_that(json.meta.all_paid).as_("all_paid").equals_to(False)
