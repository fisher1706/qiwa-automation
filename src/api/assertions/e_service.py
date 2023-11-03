import allure

from src.api.models.qiwa.e_service import admin_e_services, admin_groups_list
from src.api.payloads.e_service.groups import Group
from utils.assertion import assert_that


@allure.step
def assert_created_group(actual: dict, expected: Group) -> None:
    assert_that(actual["data"]).has("type")("group")
    (
        assert_that(actual["data"]["attributes"])
        .has("title")(expected.title_en)
        .has("description")(expected.description_en)
        .has("rules")(expected.rules_en)
        .has("message")(expected.message_en)
        .has("image")(expected.image)
        .has("state")("active")
    )
    assert_that(actual["data"]["relationships"]["e-services"]["data"]).size_is(
        len(expected.e_services)
    )
    (
        assert_that(actual["data"]["relationships"]["e-services"]["data"][0])
        .has("id")(expected.e_services[0].id)
        .has("type")("e-service")
    )
    assert_that(actual["included"]).size_is(len(expected.e_services))
    (
        assert_that(actual["included"][0])
        .has("id")(expected.e_services[0].id)
        .has("type")("e-service")
    )
    assert_that(actual["included"][0]["attributes"]).has("id")(int(expected.e_services[0].id))


@allure.step
def assert_sorting_by_position(actual: admin_e_services | admin_groups_list) -> None:
    actual_order = [item.attributes.position for item in actual.data]
    actual_positions = [position for position in actual_order if position]
    if actual_positions:
        assert_that(actual_order).as_("positions order").equals_to(
            sorted(
                actual_order,
                key=lambda position: position if position else max(actual_positions) + 1,
            )
        )
