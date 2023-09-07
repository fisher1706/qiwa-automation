import dataclasses

from selene import be, have, query
from selene.support.shared.jquery_style import s, ss

from data.dataportal.constants import (
    CustomizeModal,
    EmployeesChart,
    EstablishmentsChart,
    WorkforceChart,
)


@dataclasses.dataclass
class EmployeesChartLocators:
    TOTAL = s('//div[@id="employees-statistics"]//*[@class="chart-legends-item-value"]')
    TITLE = s('//div[@class=" employees-statistics-header"]')
    EMPLOYEE_TAB = s('(//div[@class=" employees-statistics-header"]//div//div)[1]')
    GENDER_TAB = s('(//div[@class=" employees-statistics-header"]//div//div)[2]')
    DATE_DROPDOWN = s('(//div[@id="employees-statistics"]//div[@class="dropdown"])[2]')
    LAST_YEAR_OPTION = s('((//div[@id="establishments"]//div[@class="dropdown"])[3]//li//span)[3]')
    ALL_TIME_OPTION = s('((//div[@id="establishments"]//div[@class="dropdown"])[3]//li//span)[3]')
    CUSTOM_PERIOD_OPTION = s(
        '((//div[@id="employees-statistics"]//div[@class="dropdown"])[2]//li//span)[4]'
    )
    TOTAL_MALE = s('(//div[@class="chart-legends line"]//*[@class="chart-legends-item-value"])[1]')
    TOTAL_FEMALE = s(
        '(//div[@class="chart-legends line"]//*[@class="chart-legends-item-value"])[2]'
    )


@dataclasses.dataclass
class EstablishmentsChartLocators:
    TITLE = s('//div[@class=" establishments-header"]//div')
    TOTAL = s('//div[@id="establishments"]//*[@class="chart-legends-item-value"]')
    TYPE_DROPDOWN = s('(//div[@id="establishments"]//div[@class="dropdown"])[1]')
    UNIFIED_OPTION = s('((//div[@id="establishments"]//div[@class="dropdown"])[1]//li//span)[2]')
    ENTITIES_OPTION = s('((//div[@id="establishments"]//div[@class="dropdown"])[1]//li//span)[3]')
    DATE_DROPDOWN = s('(//div[@id="establishments"]//div[@class="dropdown"])[3]')
    LAST_YEAR_OPTION = s('((//div[@id="establishments"]//div[@class="dropdown"])[3]//li//span)[2]')
    ALL_TIME_OPTION = s('((//div[@id="establishments"]//div[@class="dropdown"])[3]//li//span)[3]')
    CUSTOM_PERIOD_OPTION = s(
        '((//div[@id="establishments"]//div[@class="dropdown"])[3]//li//span)[4]'
    )


@dataclasses.dataclass
class WorkforceBySectorLocators:
    TOTAL = ss('//div[@id="workforce-statistics"]//*[@class="chart-legends-item-value"]')
    TOTAL_ALL_SECTORS_TAB = ss(
        '//div[@id="workforce-statistics"]//*[@class="helper-03 sm-label-01"]'
    )
    ALL_SECTORS = s('//div[@id="workforce-statistics"]//div/div[2]/div[2]')


class MarketOverViewPage:
    SPINNER = s("#establishments > div.chart-loader")
    CUSTOMIZE_BUTTON = s('//div[starts-with(@class, "customize-button")]')
    WORKFORCE_ALL_SECTORS = s('(//div[@id="workforce-statistics"]//div[text()])[3]')
    CUSTOMIZE_OPTION = '//span[@class="body-03-short sm-body-02-short"][contains(text(), "{0}")]'
    CUSTOMIZE_OPTIONS = '//span[@class="body-03-short sm-body-02-short"]'
    CHECKED_OPTIONS = '//div[@class="checkbox-wrapper selected"]//span[2]'
    SEARCH_FIELD = s('//div[@class="input"]/input')
    CLEAR_SEARCH_FIELD = s('//div[@class="clear-icon-wrapper"]')
    NO_RESULT_MESSAGE = s('//p[@class="body-01-highlight title"]')
    SHOW_ALL_SECTORS_BUTTON = s('//span[@class="cta-regular link primary underline c-pointer"]')
    SELECTED_OPTIONS = ss('//span[@class="cta-small"]')
    CLEAR_OPTION_BUTTONS = ss('//button[@class="clear-btn"]')
    CLEAR_OPTION_BUTTON = (
        '//span[@class="cta-small"][contains(text(), "{0}")]/../button[@class="clear-btn"]'
    )
    CLEAR_ALL_BUTTON = s('//span[@class="link secondary underline cta-regular clear-all"]')
    APPLY_BUTTON = s(
        '//button[@class="button button-large button-primary cta-regular sm-cta-large apply-btn svg-fill "]'
    )
    CLOSE_MODAL_BUTTON = s('//div[@class="c-pointer close-modal"]')
    CUSTOMIZE_INDICATOR = s('//span[@class="customize-button-indicator"]')

    """Market Overview Data locators"""
    EMPLOYEE = s('(//span[@class="num-02"])[1]')
    EMPLOYEE_5_YEARS = s('(//span[@class="num-02"])[2]')
    ESTABLISHMENTS = s('(//span[@class="num-02"])[3]')

    def __init__(self):
        super().__init__()
        self.selected_options = []
        self.options_list = []
        self.calculation = None

    def open_customize_modal(self):
        self.WORKFORCE_ALL_SECTORS.click()
        self.check_customize_state(inactive=True)
        self.CUSTOMIZE_BUTTON.click()

    def clear_searching_field(self):
        self.CLEAR_SEARCH_FIELD.click()
        actual_value = self.SEARCH_FIELD.get(query.attribute("value"))
        assert actual_value == "", f"Searching field didn't clear\nActual value: {actual_value}"

    def no_result_searching(self, message):
        no_result_message = self.NO_RESULT_MESSAGE.get(query.text)
        assert no_result_message == message, (
            f"Messages not matched\nActual message: {no_result_message}\n" f"Expected: {message}"
        )

    def check_checkbox_option(self, option):
        s(self.CUSTOMIZE_OPTION.format(option)).click()

    def get_options(self, pick_option):
        customize_options = ss(self.CUSTOMIZE_OPTIONS)
        for option in customize_options:
            self.options_list.append(option.get(query.text))
            if pick_option:
                option.click()

    def get_selected_option(self):
        for option in self.SELECTED_OPTIONS:
            self.selected_options.append(option.get(query.text))

    def clear_options(self):
        for button in self.CLEAR_OPTION_BUTTONS:
            button.click()

    @staticmethod
    def inspect_all_options_criteria(options_list, selected_options=None, selected_criteria=None):
        options_amount = len(options_list)
        assert options_amount == 20, (
            f"Invalid amount of options\nExpected: 20\n" f"Actual amount:{options_amount} "
        )
        if selected_criteria:
            assert selected_options == selected_criteria, (
                f"Options didn't match with criteria:\n"
                f"Searching criteria: {selected_criteria}\n"
                f"Selected options: {selected_options}"
            )

    def inspect_selected_option_after_apply(self, option, selected_option, multiple_options):
        if multiple_options:
            checked_options = ss(self.CHECKED_OPTIONS)
            for checked_option in checked_options:
                self.options_list.append(checked_option.get(query.text))
                assert self.options_list == option == selected_option, (
                    f"Inspected option not applied\nSetup Options:"
                    f" {option}\nChecked Option: {self.options_list}\n"
                    f"Selected Option: {selected_option}"
                )
        else:
            checked_option = s(self.CHECKED_OPTIONS).get(query.text)

            assert checked_option == option == selected_option, (
                f"Inspected option not applied\nSetup Option:"
                f" {option}\nChecked Option: {checked_option}\n"
                f"Selected Option: {selected_option}"
            )

    def check_customize_state(self, active=None, inactive=None):
        if active:
            self.CUSTOMIZE_INDICATOR.should(be.visible)
        if inactive:
            self.CUSTOMIZE_INDICATOR.should(be.not_.visible)

    @staticmethod
    def compare_lists(current_list, target_list):
        assert current_list == target_list, (
            f"Lists didn't match\n Expected list: {target_list}\n" f"Actual list: {current_list}"
        )

    def open_close_customize_modal(self):
        self.open_customize_modal()
        self.CLOSE_MODAL_BUTTON.click()

    def check_clear_searching_field(self):
        self.open_customize_modal()
        self.SEARCH_FIELD.set_value(CustomizeModal.CRITERIA)
        self.clear_searching_field()

    def check_options_searching(self):
        self.open_customize_modal()
        self.SEARCH_FIELD.set_value(CustomizeModal.CRITERIA)
        self.get_options(False)
        self.compare_lists(self.options_list, CustomizeModal.SEARCH_RESULT)

    def check_no_result_searching(self):
        self.open_customize_modal()
        self.SEARCH_FIELD.set_value(CustomizeModal.INVALID_CRITERIA)
        self.no_result_searching(CustomizeModal.NO_RESULTS)

    def check_show_all_sectors(self):
        self.open_customize_modal()
        self.SPINNER.should(be.not_.visible)
        self.get_options(pick_option=False)
        self.SEARCH_FIELD.set_value(CustomizeModal.INVALID_CRITERIA)
        self.SHOW_ALL_SECTORS_BUTTON.click()
        self.inspect_all_options_criteria(self.options_list)

    def check_selected_options(self):
        self.open_customize_modal()
        self.SEARCH_FIELD.set_value(CustomizeModal.CRITERIA)
        self.get_options(pick_option=True)
        self.get_selected_option()
        assert set(self.options_list) == set(self.selected_options)

    def check_selected_all_options(self):
        self.open_customize_modal()
        self.check_checkbox_option(CustomizeModal.SELECT_ALL_OPTION)
        self.get_options(pick_option=False)
        self.get_selected_option()
        self.inspect_all_options_criteria(
            self.options_list, self.selected_options[0], CustomizeModal.SELECT_ALL_CRITERIA
        )

    def check_clear_each_selected_options(self):
        self.open_customize_modal()
        self.SEARCH_FIELD.set_value(CustomizeModal.CRITERIA)
        self.get_options(pick_option=True)
        self.clear_options()
        self.get_selected_option()
        self.compare_lists(self.selected_options, [])
        self.CLOSE_MODAL_BUTTON.click()
        self.check_customize_state(inactive=True)

    def check_clear_all_selected_options(self):
        self.open_customize_modal()
        self.SEARCH_FIELD.set_value(CustomizeModal.CRITERIA)
        self.get_options(pick_option=True)
        self.CLEAR_ALL_BUTTON.click()
        self.get_selected_option()
        self.compare_lists(self.selected_options, [])
        self.CLOSE_MODAL_BUTTON.click()
        self.check_customize_state(inactive=True)

    def apply_option(self):
        self.open_customize_modal()
        self.check_checkbox_option(CustomizeModal.CATERING_OPTION)
        self.APPLY_BUTTON.click()
        self.check_customize_state(active=True)
        self.open_customize_modal()
        self.get_selected_option()
        self.inspect_selected_option_after_apply(
            CustomizeModal.CATERING_OPTION, self.selected_options[0], multiple_options=False
        )

    def add_another_option(self):
        self.open_customize_modal()
        self.check_checkbox_option(CustomizeModal.CATERING_OPTION)
        self.APPLY_BUTTON.click()
        self.open_customize_modal()
        self.check_checkbox_option(CustomizeModal.FINANCE_OPTION)
        self.APPLY_BUTTON.click()
        self.open_customize_modal()
        self.get_selected_option()
        self.inspect_selected_option_after_apply(
            [CustomizeModal.CATERING_OPTION, CustomizeModal.FINANCE_OPTION],
            self.selected_options,
            multiple_options=True,
        )

    @staticmethod
    def pick_unified_option():
        EstablishmentsChartLocators.TYPE_DROPDOWN.click()
        EstablishmentsChartLocators.UNIFIED_OPTION.click()

    @staticmethod
    def pick_entities_option():
        EstablishmentsChartLocators.TYPE_DROPDOWN.click()
        EstablishmentsChartLocators.ENTITIES_OPTION.click()

    @staticmethod
    def define_action_from_dict(actions_dict, action):
        if action in actions_dict:
            actions_dict[action]()

    def define_chart_action(self, arg):
        actions_dict = {
            EmployeesChart.GO_TO_GENDER_TAB: EmployeesChartLocators.GENDER_TAB.click(),
            EstablishmentsChart.PICK_UNIFIED_OPTION: self.pick_unified_option,
            EstablishmentsChart.PICK_ENTITIES_OPTION: self.pick_entities_option,
            WorkforceChart.ALL_SECTORS: WorkforceBySectorLocators.ALL_SECTORS.click(),
        }
        self.define_action_from_dict(actions_dict, arg)

    def check_incoming_data(self, element, text, action):
        if action:
            self.define_chart_action(action)
        element.should(have.text(text))

    def check_incoming_multiple_data(self, elements, list_text, action):
        elements_list = []
        if action:
            self.define_chart_action(action)
        for element in elements:
            elements_list.append(element.get(query.text))
        assert elements_list == list_text, f"Actual:{elements_list}\nExpected:{list_text}"

    def employee_calculation(self, first_value, last_value):
        calculation = ((last_value - first_value) / first_value) * 100
        self.calculation = f"+{calculation:.0f}%"
