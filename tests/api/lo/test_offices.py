import allure

from data.lo.constants import LOSysAdmin, OfficesInfo
from src.api.app import QiwaApi


@allure.title('Get all offices')
def test_offices():
    qiwa = QiwaApi.login_as_user(personal_number=LOSysAdmin.ID)
    qiwa.offices_api_action.get_offices()


@allure.title('Create labor office')
def test_create_office(index_name="Create labor office"):
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.offices_api_action.create_office(
        office_name=OfficesInfo.OFFICES_NAME + " " + index_name,
        hourly_capacity=OfficesInfo.HOURLY_CAPACITY,
        working_hours_from=OfficesInfo.WORKING_HOURS_FROM,
        working_hours_to=OfficesInfo.WORKING_HOURS_TO,
        address=OfficesInfo.ADDRESS,
        region_id=OfficesInfo.NAJRAN_REGION_ID,
        latitude=OfficesInfo.LATITUDE,
        longitude=OfficesInfo.LONGITUDE,
        is_electronic_office=OfficesInfo.IS_ELECTRONIC_OFFICE)


@allure.title('Edit labor office')
def test_edit_office():
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.offices_api_action.edit_office(
        office_name=OfficesInfo.OFFICES_NAME,
        hourly_capacity_edited=OfficesInfo.HOURLY_CAPACITY_EDITED,
        working_hours_from_edited=OfficesInfo.WORKING_HOURS_FROM_EDITED,
        working_hours_to_edited=OfficesInfo.WORKING_HOURS_TO_EDITED,
        address_edited=OfficesInfo.ADDRESS_EDITED,
        region_id_edited=OfficesInfo.TABUK_REGION_ID,
        latitude_edited=OfficesInfo.LATITUDE_EDITED,
        longitude_edited=OfficesInfo.LONGITUDE_EDITED)


@allure.title('Change labor office status')
def test_change_office_status(index_name="Change status"):
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.offices_api_action.create_office(
        office_name=OfficesInfo.OFFICES_NAME + " " + index_name,
        hourly_capacity=OfficesInfo.HOURLY_CAPACITY,
        working_hours_from=OfficesInfo.WORKING_HOURS_FROM,
        working_hours_to=OfficesInfo.WORKING_HOURS_TO,
        address=OfficesInfo.ADDRESS,
        region_id=OfficesInfo.NAJRAN_REGION_ID,
        latitude=OfficesInfo.LATITUDE,
        longitude=OfficesInfo.LONGITUDE,
        is_electronic_office=OfficesInfo.IS_ELECTRONIC_OFFICE)
    qiwa.offices_api_action.change_office_status()
