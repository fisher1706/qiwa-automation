from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s

from data.constants import Language
from data.lo.constants import AppointmentsView as Av


class LaborOfficeAppointmentsViewPage:
    def __init__(self):
        self.language = Language.EN

    appointments_view_pagination = s(
        "//*[@id='root']/div/span/div[1]/div/span[1]/div/div/div/div[1]/nav/ol"
    )

    appointment_reference_number = s("//*[@role='status']//div/div/p[1]")
    info_row_text = s("//*[@role='status']//div/div/p[2]")

    general_info_date_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[1]/td/div/p[1]"
    )
    general_info_date_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[1]/td/div/p[1]"
    )
    general_info_time_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[2]/td/div/p[1]"
    )
    general_info_time_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[2]/td/div/p[2]"
    )
    general_info_service_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[3]/td/div/p[1]"
    )
    general_info_service_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[3]/td/div/p[2]"
    )
    general_info_sub_service_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[4]/td/div/p[1]"
    )
    general_info_sub_service_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[4]/td/div/p[2]"
    )
    general_info_office_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[5]/td/div/p[1]"
    )
    general_info_office_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[5]/td/div/p[2]"
    )
    general_info_location_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[6]/td/div/p[1]"
    )
    general_info_location_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[6]/td/div/div/a/span"
    )
    general_info_type_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[7]/td/div/p[1]"
    )
    general_info_type_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[7]/td/div/p[2]"
    )
    general_info_status_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[8]/td/div/p[1]"
    )
    general_info_status_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[1]/div/div/div[3]/table/tbody/tr[8]/td/div/div/p"
    )

    requester_type_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[2]/div/div/div/table/tbody/tr[1]/td/div/p[1]"
    )
    requester_type_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[2]/div/div/div/table/tbody/tr[1]/td/div/p[2]"
    )
    requester_id_text = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[2]/div/div/div/table/tbody/tr[2]/td/div/p[1]"
    )
    requester_id_value = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]"
        "/div[2]/div/div/div/table/tbody/tr[2]/td/div/p[2]"
    )

    show_map_btn = s(
        "//*[@id='root']/div/span/div[1]/div/span[2]/div[1]/div/div/div[3]/"
        "table/tbody/tr[6]/td/div/div/a"
    )
    close_map_btn = s("//*[@id='modalBodyWrapper']/div[1]/button")
    map_get_link_btn = s("//*[@id='modalBodyWrapper']/div[3]/button")
    map_text_row = s("//*[@id='modalBodyWrapper']/div[2]/div[1]").ss("p")
    map_title = map_text_row.first
    map_text = map_text_row.second
    map_body = s("//*[@id='modalBodyWrapper']/div[2]/div[2]")
    map_blue_pin_btn = s(
        "//*[@id='modalBodyWrapper']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/div"
    )
    map_addres_detailes_form = s(
        "//*[@id='modalBodyWrapper']/div[2]/div[2]/div/div/div[2]/div[2]/div/"
        "div[4]/div/div/div/div[1]"
    )
    copy_map_form_text = s("//*[@id='root']/div[3]/div/div/div/div")

    print_bnt = s(
        "//*[@id='root']/div/span/div[1]/div/span[1]/div/div/div/div[2]/div[2]/div/button[1]"
    )

    @allure.step("Verify last element of pagination text")
    def verify_pagination(self, text: dict, locale: str):
        self.appointments_view_pagination.should(have.text(text[locale]))

    @allure.step("Verify appointment reference number text")
    def verify_appointment_reference_number(self, text: dict, locale: str):
        self.appointment_reference_number.should(have.text(text[locale]))

    @allure.step("Verify info row text")
    def verify_info_row_text(self, text: dict, locale: str):
        self.info_row_text.should(have.text(text[locale]))

    @allure.step("Verify date text text")
    def verify_general_info_date_text(self, text: dict, locale: str):
        self.general_info_date_text.should(have.text(text[locale]))

    @allure.step("Verify time text")
    def verify_general_info_time_text(self, text: dict, locale: str):
        self.general_info_time_text.should(have.text(text[locale]))

    @allure.step("Verify service text")
    def verify_general_info_service_text(self, text: dict, locale: str):
        self.general_info_service_text.should(have.text(text[locale]))

    @allure.step("Verify sub service text")
    def verify_general_info_sub_service_text(self, text: dict, locale: str):
        self.general_info_sub_service_text.should(have.text(text[locale]))

    @allure.step("Verify office text")
    def verify_general_info_office_text(self, text: dict, locale: str):
        self.general_info_office_text.should(have.text(text[locale]))

    @allure.step("Verify location text")
    def verify_general_info_location_text(self, text: dict, locale: str):
        self.general_info_location_text.should(have.text(text[locale]))

    @allure.step("Verify type text")
    def verify_general_info_type_text(self, text: dict, locale: str):
        self.general_info_type_text.should(have.text(text[locale]))

    @allure.step("Verify status text")
    def verify_general_info_status_text(self, text: dict, locale: str):
        self.general_info_status_text.should(have.text(text[locale]))

    @allure.step("Verify requester type text")
    def verify_requester_type_text(self, text: dict, locale: str):
        self.requester_type_text.should(have.text(text[locale]))

    @allure.step("Verify requester id text")
    def verify_requester_id_text(self, text: dict, locale: str):
        self.requester_id_text.should(have.text(text[locale]))

    @allure.step("Open map")
    def open_map(self):
        self.show_map_btn.click()

    @allure.step("Verify mamp title text")
    def verify_map_title(self, text: dict, locale: str):
        self.map_title.should(have.text(text[locale]))

    @allure.step("Verify map text")
    def verify_map_text(self, text: dict, locale: str):
        self.map_text.should(have.text(text[locale]))

    @allure.step("Verify copy map form text")
    def verify_copy_map_form_text(self, text: dict, locale: str):
        self.copy_map_form_text.should(have.text(text[locale]))

    @allure.step("Open print")
    def open_print(self):
        self.print_bnt.click()

    @allure.step("Verify print button exists")
    def verify_print_btn(self):
        self.print_bnt.should(be.visible)

    @allure.step("Verify general info row text and valuers exists")
    def verify_general_info_row(self):
        self.verify_pagination(Av.PAGINATION, self.language)
        self.verify_appointment_reference_number(Av.APPOINTMENT_REFERENCE_NUMBER, self.language)
        self.verify_info_row_text(Av.INFO_ROW_TEXT, self.language)

    @allure.step("Verify general table text and valuers exists")
    def verify_general_table(self):
        self.verify_general_info_date_text(Av.GENERAL_INFO_DATA_TEXT, self.language)
        self.general_info_date_value.should(be.visible)
        self.verify_general_info_time_text(Av.GENERAL_INFO_TIME_TEXT, self.language)
        self.general_info_time_value.should(be.visible)
        self.verify_general_info_service_text(Av.GENERAL_INFO_SERVICE_TEXT, self.language)
        self.general_info_service_value.should(be.visible)
        self.verify_general_info_sub_service_text(Av.GENERAL_INFO_SUB_SERVICE_TEXT, self.language)
        self.general_info_sub_service_value.should(be.visible)
        self.verify_general_info_office_text(Av.GENERAL_INFO_OFFICE_TEXT, self.language)
        self.general_info_office_value.should(be.visible)
        self.verify_general_info_location_text(Av.GENERAL_INFO_LOCATION_TEXT, self.language)
        self.general_info_location_value.should(be.visible)
        self.verify_general_info_type_text(Av.GENERAL_INFO_TYPE_TEXT, self.language)
        self.general_info_status_value.should(be.visible)
        self.verify_general_info_status_text(Av.GENERAL_INFO_STATUS_TEXT, self.language)

    @allure.step("Verify requester info text and valuers exists")
    def verify_requester_info(self):
        self.verify_requester_type_text(Av.REQUESTER_TYPE, self.language)
        self.requester_type_value.should(be.visible)
        self.verify_requester_id_text(Av.REQUESTER_ID, self.language)
        self.requester_id_value.should(be.visible)

    @allure.step("Verify map elements text and valuers exists")
    def verify_map_elements(self):
        self.open_map()
        self.verify_map_title(Av.MAP_TITLE, self.language)
        self.verify_map_text(Av.MAP_TEXT, self.language)
        self.close_map_btn.should(be.visible)
        self.map_body.should(be.visible)
        self.map_get_link_btn.should(be.visible)
        self.close_map_btn.click()
        self.verify_general_info_row()

    @allure.step("Verify map functions")
    def verify_map_functions(self):
        self.open_map()
        self.map_blue_pin_btn.click()
        self.map_addres_detailes_form.should(be.visible)
        self.map_get_link_btn.click()
        self.verify_copy_map_form_text(Av.COPY_MAP_TEXT, self.language)
        self.close_map_btn.click()
        self.verify_general_info_row()