import allure
from selene.api import be, command, have, query, s, ss

from data.visa.constants import ISSUE_VISA_REQUEST_TITLE, Numbers
from src.ui.components.feedback_pop_up import FeedbackPopup


class IssueVisaPage:
    loading = ss(
        '//*[@class="react-loading-skeleton" or starts-with(@class, "Loader__LoaderWrapper")]'
    )
    network_failed = ss('//p[@id="baseAutocomplete-error"]')
    title = s(f'//*[contains(text(), "{ISSUE_VISA_REQUEST_TITLE}")]')
    dropdowns = ss('//*[@id="autocomplete"]')
    dropdown_form = s('//*[@data-testid="visaDetailsFormWrapper"]')
    dropdown_occupation = s('//*[@data-testid="occupationsAutocomplete"]')
    dropdown_nationality = s('//*[@data-testid="nationalitiesAutocomplete"]')
    dropdown_embassy = s('//*[@data-testid="embassiesAutocomplete"]')
    dropdown_options = ss('//*[@class="tippy-content"]//li')
    amount_input = s('//*[@id="visas-amount-select"]')
    add_button = s('//*[@data-testid="formSubmitAddVisaDetails"]')
    requests_table = s('//*[@data-testid="addedVisasTable"]')
    next_step_button = s('//*[@data-testid="nextStepBtn"]')
    visa_request_table = s('//*[@id="addedVisasTable"]')
    accept_checkbox = s('//*[@data-testid="iHaveReadAndAcceptTerms"]/following-sibling::span')
    submit_button = s('//*[@data-testid="submitVisaRequestsBtn"]')
    request_created_banner = s('//*[@data-testid="yourRequestForPaymentWorkVisasApproved"]')
    visa_request_ref_number = s('//*[@data-testid="yourRequestForPaymentWorkVisasApproved"]//span')
    back_to_perm_work_visas = s('//*[@data-testid="backToWorkVisas"]')
    popup = FeedbackPopup('//*[@data-component="Modal"]')

    @allure.step("Verify issue visa page is open")
    def verify_issue_visa_page_open(self):
        self.loading.should(have.size_greater_than(0))
        self.loading.should(have.size(0))
        self.title.should(be.visible)

    @allure.step("Create permanent work visa request")
    def create_perm_visa_request(self):
        for dropdown in self.dropdowns:
            dropdown.click()
            self.dropdown_options.first.click()
        self.amount_input.type(Numbers.ONE)
        self.add_button.click()
        self.requests_table.should(be.visible)
        self.next_step_button.should(be.visible).should(be.clickable)
        command.js.scroll_into_view(self.visa_request_table)
        self.next_step_button.click()
        self.visa_request_table.should(be.visible)
        self.accept_checkbox.should(be.visible)
        self.accept_checkbox.click()
        self.submit_button.click()
        self.popup.close_feedback()
        self.request_created_banner.should(be.visible)
        ref_number = self.visa_request_ref_number.get(query.text)
        self.back_to_perm_work_visas.click()
        return ref_number

    @allure.step("Verify lazy loading")
    def verify_lazy_loading(self):
        command.js.scroll_into_view(self.dropdown_form)
        self.verify_lazy_loading_dropdown(self.dropdown_occupation)
        self.verify_lazy_loading_dropdown(self.dropdown_nationality)
        self.verify_lazy_loading_dropdown(self.dropdown_embassy)

    def verify_lazy_loading_dropdown(self, dropdown):
        dropdown.click()
        self.dropdown_options.should(have.size(Numbers.LAZYLOADING_PACK_SIZE))
        self.dropdown_options.first.hover()
        command.js.scroll_into_view(
            self.dropdown_options.element(Numbers.LAZYLOADING_PACK_SIZE - 1)
        )
        self.dropdown_options.should(have.size(2 * Numbers.LAZYLOADING_PACK_SIZE))
        dropdown.click()
        self.dropdown_options.should(have.size(Numbers.ZERO))
