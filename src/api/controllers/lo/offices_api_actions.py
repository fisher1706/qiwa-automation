import allure

from src.api.clients.lo.offices import OfficesApi
from src.api.clients.lo.services import ServicesApi


class OfficesApiActions(OfficesApi):
    def __init__(self, api):
        super().__init__(api)
        self.service_api = ServicesApi(api)

    @allure.step("I create labor office")
    def create_office(
        self,
        office_name,
        hourly_capacity,
        working_hours_from,
        working_hours_to,
        address,
        region_id,
        latitude,
        longitude,
        is_electronic_office=False,
    ):
        last_service_id = self.service_api.get_last_service_id()
        office_id = self.post_office(
            office_name=office_name,
            hourly_capacity=hourly_capacity,
            working_hours_from=working_hours_from,
            working_hours_to=working_hours_to,
            address=address,
            region_id=region_id,
            latitude=latitude,
            longitude=longitude,
            service_id=last_service_id,
            is_electronic_office=is_electronic_office,
        )
        self.get_office(office_id)
        office_attribute_name = self.office["data"]["attributes"]["office-name"]
        office_attribute_hourly_capacity = self.office["data"]["attributes"]["hourly-capacity"]
        office_attribute_working_hours_from = self.office["data"]["attributes"][
            "working-hours-from"
        ]
        office_attribute_working_hours_to = self.office["data"]["attributes"]["working-hours-to"]
        office_attribute_address = self.office["data"]["attributes"]["gmap-address"]
        office_attribute_region_id = self.office["data"]["attributes"]["region-id"]
        office_attribute_latitude = self.office["data"]["attributes"]["latitude"]
        office_attribute_longitude = self.office["data"]["attributes"]["longitude"]
        office_attribute_is_electronic_office = self.office["data"]["attributes"][
            "is-electronic-office"
        ]
        office_attribute_last_service_id = self.office["data"]["relationships"]["services"][
            "data"
        ][0]["id"]
        assert office_attribute_name == office_name
        assert office_attribute_hourly_capacity == hourly_capacity
        assert office_attribute_working_hours_from == working_hours_from
        assert office_attribute_working_hours_to == working_hours_to
        assert office_attribute_address == address
        assert office_attribute_region_id == region_id
        assert office_attribute_latitude == latitude
        assert office_attribute_longitude == longitude
        assert office_attribute_is_electronic_office == is_electronic_office
        assert office_attribute_last_service_id == last_service_id

    @allure.step("I edit list of fields of later labor office")
    def edit_office(
        self,
        office_name,
        hourly_capacity_edited,
        working_hours_from_edited,
        working_hours_to_edited,
        address_edited,
        region_id_edited,
        latitude_edited,
        longitude_edited,
    ):
        last_service_id = self.service_api.get_last_service_id()
        self.get_offices()
        self.put_edit_office(
            office_name=office_name,
            hourly_capacity=hourly_capacity_edited,
            working_hours_from=working_hours_from_edited,
            working_hours_to=working_hours_to_edited,
            address=address_edited,
            region_id=region_id_edited,
            latitude=latitude_edited,
            longitude=longitude_edited,
            service_id=last_service_id,
            office_id=self.last_office_id,
        )
        self.get_office(self.last_office_id)
        office_attribute_name = self.office["data"]["attributes"]["office-name"]
        office_attribute_hourly_capacity = self.office["data"]["attributes"]["hourly-capacity"]
        office_attribute_working_hours_from = self.office["data"]["attributes"][
            "working-hours-from"
        ]
        office_attribute_working_hours_to = self.office["data"]["attributes"]["working-hours-to"]
        office_attribute_address = self.office["data"]["attributes"]["gmap-address"]
        office_attribute_region_id = self.office["data"]["attributes"]["region-id"]
        office_attribute_latitude = self.office["data"]["attributes"]["latitude"]
        office_attribute_longitude = self.office["data"]["attributes"]["longitude"]
        office_attribute_service_id = int(
            self.office["data"]["relationships"]["services"]["data"][1]["id"]
        )
        assert office_attribute_name == office_name
        assert office_attribute_hourly_capacity == hourly_capacity_edited
        assert office_attribute_working_hours_from == working_hours_from_edited
        assert office_attribute_working_hours_to == working_hours_to_edited
        assert office_attribute_address == address_edited
        assert office_attribute_region_id == region_id_edited
        assert office_attribute_latitude == latitude_edited
        assert office_attribute_longitude == longitude_edited
        assert office_attribute_service_id == int(last_service_id) - 1

    @allure.step("I get current status, reversed it and setup for labor office")
    def change_office_status(self):
        self.get_offices()
        self.get_office(self.last_office_id)
        reverse_office_status = self.office_status is False
        self.patch_office_status(self.last_office_id, reverse_office_status)
        self.get_office(self.last_office_id)
        office_attribute_reverse_office_status = self.office["data"]["attributes"]["is-active"]
        assert office_attribute_reverse_office_status == reverse_office_status
        self.patch_office_status(self.last_office_id, not self.office_status)
