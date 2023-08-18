import allure
from selene import browser

from helpers.assertion import assert_that
from src.ui.pages.dashboard_page import DashboardPage
from src.ui.pages.e_services_page import EServicesPage


class EServiceActions(EServicesPage):
    def __init__(self):
        super().__init__()
        self.dashboard_page = DashboardPage()

    @allure.step("Select e-service")
    def select_e_service(self, e_service_name):
        self.dashboard_page.select_e_services_menu_item()
        self.click_on_e_service(e_service_name)

    @allure.step("I switch to e-services")
    def switch_to_e_services(self) -> EServicesPage:
        self.dashboard_page.select_e_services_menu_item()
        return self

    @allure.step("Search e-service by name")
    def search_by_category_name(self, category_name):
        self.search_elements_by_title(category_name)
        self.parse_e_services_and_button_status()

        assert (
            len(self.e_services_status_dict) == 1
        ), f"More than 1 e-service found after search by [{category_name}]: {self.e_services_status_dict}"
        service_name = self.e_services_status_dict[0]["name"]
        if category_name:
            assert (
                service_name.lower() == category_name.lower()
            ), f"E-service {service_name} is not in the list: {category_name}"
        else:
            assert (
                service_name == category_name
            ), f"E-service [{service_name}] not equal to {category_name}"

    @allure.step
    def delete_e_service_by_en_title(self, title):
        self.enter_e_service_en_filter(title)
        self.click_delete_e_service()
        alert = browser.switch_to.alert
        assert_that(alert.text).as_("Alert message").equals_to(
            "Are you sure you want to delete this service?"
        )
        alert.accept()
