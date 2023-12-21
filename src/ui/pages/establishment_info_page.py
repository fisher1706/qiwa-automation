from __future__ import annotations

from selene import be, command, have
from selene.support.shared.jquery_style import s, ss

from data.user_management import user_management_data


class EstablishmentInfoPage:
    title_on_establishment_page = s("[data-component='Layout'] h1")
    financial_info_section = s("#financial-information-section")
    change_establishment_address_link = "[data-component='Link']"
    city_input = s("[name='city']")
    dropdown_option = s("[role='option']")
    district_input = s("[name='district']")
    street_input = s("[name='streetName']")
    building_number_input = s("[name='buildingNumber']")
    additional_number_input = s("[name='additionalNumber']")
    submit_btn = s("[type='submit']")
    thank_you_title = s("[role='heading']")
    establishment_data_values_on_thank_you_popup = ss("p.fVmszV")
    buttons_on_thank_you_popup = ss("[data-component='Button']")

    def check_financial_info_section_is_displayed(self) -> EstablishmentInfoPage:
        self.title_on_establishment_page.should(
            have.text(user_management_data.ESTABLISHMENT_INFO_TITLE)
        )
        self.financial_info_section.should(be.visible)
        self.financial_info_section.s("h2").should(
            have.text(user_management_data.FINANCIAL_INFO_SECTION)
        )
        return self

    def click_change_establishment_address_link(self) -> EstablishmentInfoPage:
        self.financial_info_section.s(self.change_establishment_address_link).click()
        return self

    def enter_all_establishment_data(
        self, city: str, district: str, street: str, building_no: str, additional_no: str
    ) -> EstablishmentInfoPage:
        self.city_input.send_keys(city)
        self.dropdown_option.click()
        self.district_input.send_keys(district)
        self.street_input.send_keys(street)
        self.building_number_input.send_keys(building_no)
        self.additional_number_input.set_value(additional_no)
        return self

    def update_district_and_street_data(
        self, city: str, district: str, street: str
    ) -> EstablishmentInfoPage:
        self.city_input.send_keys(city)
        self.dropdown_option.click()
        self.district_input.perform(command.js.set_value("")).type(district)
        self.street_input.perform(command.js.set_value("")).type(street)
        return self

    def click_submit_btn(self) -> EstablishmentInfoPage:
        self.submit_btn.click()
        return self

    def check_establishment_data_on_thank_you_popup(
        self, establishment_values: list
    ) -> EstablishmentInfoPage:
        self.thank_you_title.should(have.text(user_management_data.THANK_YOU_TITLE))
        for establishment_value in establishment_values:
            self.establishment_data_values_on_thank_you_popup.element_by(
                have.text(establishment_value)
            ).should(be.visible)
        return self

    def click_back_to_subscription_flow_btn(self) -> EstablishmentInfoPage:
        self.buttons_on_thank_you_popup.element_by(
            have.text(user_management_data.BACK_TO_SUBSCRIPTION_BTN)
        ).click()
        return self
