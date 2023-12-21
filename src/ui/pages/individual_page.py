from __future__ import annotations

import time

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.keys import Keys

from data.constants import Language
from src.ui.components.meet_qiwa_popup import MeetQiwaPopup
from src.ui.components.raw.table import Table
from utils.allure import allure_steps


@allure_steps
class IndividualPage:
    service_card = ss('[data-component="ActionTile"] div')
    field_confirmation_code = ss('[inputmode="numeric"]')
    checkbox_agree = s("#termsOfService")
    btn_accept_the_request = s('//button[.="Accept"]')
    btn_reject_the_request = s('//button[.="Reject"]')
    btn_modal_accept_the_request = s('//button[.="Accept transfer"]')
    btn_modal_reject_the_request = s('//button[.="Reject transfer"]')
    # TODO(dp): Redesign elements using raw dropdown
    dropdown_modal_reject_reason = s("#reasonType")
    dropdown = s(".tippy-content")
    locale = s("#language-select")
    modal = s(".basic-modal__header")
    modal_meet_qiwa = s('//*[@data-component="Modal"]')
    individual_table = Table(s(".table"))
    status = s('[role="status"]')
    see_all_services = s('//a[@href="/services"]')
    go_to_resume_management = s("//p[normalize-space()='Go to Resume Management']")
    services = s("//p[normalize-space()='Services']")
    links = ss("[data-component='Menu'] a")
    lang_links = {
        Language.EN: links.first,
        Language.AR: links.second,
    }

    def navigate_to_services(self) -> IndividualPage:
        self.services.click()
        return self

    @allure.step("Wait Individual page to load")
    def wait_page_to_load(self) -> IndividualPage:
        self.service_card.first.should(be.present)
        MeetQiwaPopup().close_meet_qiwa_popup_if_displayed()
        return self

    @allure.step("Click on See all services")
    def click_see_all_services(self) -> IndividualPage:
        self.see_all_services.click()
        self.service_card.first.should(be.visible)
        return self

    def select_service(self, text: str) -> IndividualPage:
        self.service_card.element_by(have.text(text)).wait_until(be.visible)
        self.service_card.element_by(have.text(text)).click()
        return self

    def click_agree_checkbox(self) -> IndividualPage:
        self.checkbox_agree.press(Keys.SPACE)
        return self

    def click_btn_accept_the_request(self) -> IndividualPage:
        self.btn_accept_the_request.click()
        return self

    def click_btn_reject_the_request(self) -> IndividualPage:
        self.btn_reject_the_request.click()
        return self

    def click_btn_modal_accept_the_request(self) -> IndividualPage:
        self.btn_modal_accept_the_request.click()
        return self

    def click_btn_modal_reject_the_request(self) -> IndividualPage:
        self.btn_modal_reject_the_request.click()
        return self

    def verify_expected_status(self, text: str) -> IndividualPage:
        # TODO(dp): Remove this sleep after fixing an issue with the shown section
        time.sleep(5)
        browser.driver.refresh()
        self.status.should(have.text(text))
        return self

    def select_rejection_reason(self, reason: str) -> IndividualPage:
        self.dropdown_modal_reject_reason.click()
        self.dropdown.all('[role="option"]').element_by(have.text(reason)).click()
        return self

    def wait_until_popup_disappears(self) -> IndividualPage:
        self.modal.wait_until(be.not_.visible)
        return self

    def navigate_to_resume_management(self) -> IndividualPage:
        self.go_to_resume_management.click()
        return self
