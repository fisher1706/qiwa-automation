from __future__ import annotations

import time

import allure
from selene import be, query
from selene.support.shared.jquery_style import s, ss

from data.constants import EService, EServiceAction


class EServicesPage:
    VISA_ISSUANCE = "#visa_issuance .q-page-box__footer button"
    SEARCH_FIELD = '[placeholder="Search"]'
    NATIONAL_ADDRESS_REG = "#saudi_post .q-page-box__footer button"
    REQUEST_BUTTON = "#link_1"
    REQUEST_SECOND_BUTTON = "#link_2"
    VIEW_REQUESTS_BUTTON = "li:last-child .request_list-btn"
    POPUP = '[aria-expanded="true"] > .rules-modal'
    RULES_LIST = '[aria-expanded="true"] .rules-list_item'
    REQUEST_SERVICES_BUTTON = ".q-page-box__footer button"
    LINK_CONTRACT_MANAGEMENT = '[title="Contract Management"]'
    ESERVICES_LIST = ".q-page-box .service-item"
    SERVICE_TITLE = ".text--regular"
    SERVICE_BUTTON = ".q-btn--primary"
    RESEND_VERIFICATION_EMAIL_BUTTON = '//*[@class="q-btn with-preloader-color"]'
    EMAIL_ADDRESS_FIELD = ".verify__content__head__email span"
    VERIFICATION_EMAIL_POPUP = ".verify-block__box"
    SEARCH_BUTTON = ".icon-search"
    ESERVICES_FILTER_BUTTONS = ".eServices-page__sort-holder__tags > div > button"
    e_services = {
        EService.CHANGE_OCCUPATION: f"#change_occupation {REQUEST_SERVICES_BUTTON}",
        EService.NITAQAT_CALCULATOR: f"#nitaqat_calculator {REQUEST_SERVICES_BUTTON}",
        EService.WORK_PERMIT: f"#working_permits {REQUEST_SERVICES_BUTTON}",
        EService.TRANSFER_WORKER: f"#transferring_worker {REQUEST_SERVICES_BUTTON}",
        EService.SAUDIZATION_CERTIFICATE: f"#saudization_certificate {REQUEST_SERVICES_BUTTON}",
        EService.USER_MANAGEMENT: f"#subscription_service {REQUEST_SERVICES_BUTTON}",
        EService.VALIDATION_CERTIFICATE: f"#validation_certificate {REQUEST_SERVICES_BUTTON}",
        EService.EMPLOYEE_TRANSFER: f"#employee_transfer {REQUEST_SERVICES_BUTTON}",
        EService.CONTRACT_MANAGEMENT: f"#contract_management {REQUEST_SERVICES_BUTTON}",
        # Uncomment after clarifying difference between envs
        # EService.CONTRACT_MANAGEMENT: LINK_CONTRACT_MANAGEMENT
    }
    LOCK_E_SERVICES_MESSAGE = ".renew-subscription-block__content"
    LOCK_E_SERVICES_LINK = ".q-btn--link"
    ADD_E_SERVICE_BUTTON = ".button-block .btn:first-child"
    # add e-service form
    PERMISSION_CHECKBOX = "label.checkbox__label"
    TITLE_ENGLISH_FIELD = '[data-vv-as="Name English"]'
    TITLE_ARABIC_FIELD = '[data-vv-as="Name Arabic"]'
    SERVICE_CODE_FIELD = '[data-vv-as="Service Code"]'
    ENGLISH_LINK_FIELD = '[data-vv-as="English link name"]'
    ARABIC_LINK_FIELD = '[data-vv-as="Arabic link name"]'
    LINK_URL_FIELD = '[data-vv-as="link URL"]'
    CREATE_E_SERVICE_BUTTON = ".mt-4 .btn--primary"
    EN_TITLE_FILTER_FIELD = "#titleEn"
    EN_TITLE_FIRST_RECORD = '[data-label="E-services title (English) "] > span'
    RESULTS_COUNT = ".footer-left"
    DELETE_E_SERVICE_BUTTON = '[data-label="Actions"] button'
    E_SERVICES_LIST = {
        "active": ".eServices-page__active-eservices div h2",
        "forbidden": ".eServices-page__forbidden-eservices div h2",
    }
    EMPLOYEE_TRANSFER_CARD = s("//p[.='Employee Transfer']")
    CERTIFICATES_CARD = s("//p[.='Certificates'']")
    LO = s("//p[.='Labor Office Appointments']")

    def __init__(self):
        super().__init__()
        self.page_url = "/en/company/e-services/"
        self.e_services_status_dict = []

    def click_on_e_service(self, e_service_name):
        s(self.e_services[e_service_name]).should(be.clickable).click()

    def click_submit_request(self):
        s(self.REQUEST_BUTTON).should(be.clickable).click()

    def click_submit_request_second(self):
        s(self.REQUEST_SECOND_BUTTON).should(be.clickable).click()

    def click_view_requests(self):
        s(self.VIEW_REQUESTS_BUTTON).should(be.clickable).click()

    def perform_e_service_action(self, action_name):
        e_service_action = {
            EServiceAction.TRANSFER_TO_COMPANY: self.click_submit_request,
            EServiceAction.TRANSFER_BETWEEN_BRANCHES: self.click_submit_request_second,
            EServiceAction.SUBMIT_REQUEST: self.click_submit_request,
            EServiceAction.VIEW_REQUEST: self.click_view_requests,
            EServiceAction.ESTABLISHMENTS_USERS: self.click_submit_request,
            EServiceAction.SUBSCRIBE_NEW_USER: self.click_submit_request_second,
        }
        e_service_action[action_name]()

    @allure.step
    def parse_e_services_and_button_status(self):
        e_services_list = ss(self.ESERVICES_LIST)
        time.sleep(1)
        if len(e_services_list) == 0:
            self.e_services_status_dict = []
            return self
        e_services_list.first.s(self.SERVICE_TITLE).should(be.visible)  # pylint: disable = E1101
        self.e_services_status_dict = []
        for service in e_services_list:
            self.e_services_status_dict.append(
                {
                    "name": service.s(self.SERVICE_TITLE).get(query.text),
                    "status": service.s(self.SERVICE_BUTTON).should(be.enabled),
                }
            )
        return None

    def search_elements_by_title(self, searched_element_name):
        s(self.SEARCH_FIELD).should(be.visible).should(be.blank).type(searched_element_name)
        s(self.SEARCH_BUTTON).should(be.clickable).click()

    @allure.step("Filter e-service by title")
    def enter_e_service_en_filter(self, name: str) -> EServicesPage:
        s(self.EN_TITLE_FILTER_FIELD).should(be.visible).type(name)
        time.sleep(3)
        return self

    def click_delete_e_service(self) -> EServicesPage:
        s(self.DELETE_E_SERVICE_BUTTON).with_(timeout=1).should(be.clickable).click()
        return self

    def select_employee_transfer(self):
        self.EMPLOYEE_TRANSFER_CARD.click()

    def select_certificates(self):
        self.CERTIFICATES_CARD.click()

    def select_lo(self):
        self.LO.click()