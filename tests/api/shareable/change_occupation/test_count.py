from data.shareable.change_occupation import RequestStatus
from utils.assertion import assert_that
from utils.json_search import get_data_attribute


def test_getting_requests_count(change_occupation):
    json = change_occupation.get_requests_count()
    assert_that(json.data).size_is(len(RequestStatus))

    status_ids_in_json = get_data_attribute(json, "status_id")
    assert_that(status_ids_in_json).equals_to(RequestStatus.values())
