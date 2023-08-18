from selene import be, by
from selene.support.shared.jquery_style import s


class DashboardLocators:  # pylint: disable=too-few-public-methods
    DASHBOARD_PAGE = by.xpath('//*[@alt="Dashboard"]')
    COMMERCIAL_RECORD_NUMBER = ".header--big"
    SWITCH_ACCOUNT_LINK = by.css(".dropdown-menu div:nth-child(1) > a")
    SAUDI_CERTIFICATE_NUMBER = "#saudization-certificate .q-page-box__list_item:first-child dd"
    E_SERVICES_MENU = by.css('.q-navigation__list_item img[alt="E-services"]')
    ADMIN_E_SERVICES_MENU = by.css("#eservices")
    ESTABLISHMENT_INFO_MENU = by.css(
        '.q-navigation__list_item img[alt="Establishment information"]'
    )
    CONFIRM_EMAIL_TEXT = by.xpath('//*[@class="mb-0"]')
    ARABIC_LANGUAGE_BUTTON = by.xpath('//*[@class="q-langs-switcher"]/li[2]/button')
    ENGLISH_LANGUAGE_BUTTON = by.xpath('//*[@class="q-langs-switcher"]/li[1]/button')
    EXPAT_EMPLOYEES_DETAILS_BUTTON = by.xpath('//*[@href="https://employee-details.qiwa.tech"]')
    CONTROL_PANEL = by.xpath('//*[@alt="Control Panel"]')
    COMPANY_NAMES_LIST = by.xpath('//*[@class="VueCarousel workspaces-list"]')

    # TITLES
    COMPANY_PROFILE_TITLE = by.css(".company-information .q-page-box__header")
    COMMERCIAL_RECORD_TITLE = by.css(".commercial-record .q-page-box__title")
    SAUDI_CERTIFICATE_TITLE = by.css("#saudization-certificate h2")
    WAGE_PROTECTION_SYSTEM_CERTIFICATE_TITLE = by.css(
        "#safeguardingwages-certificate .q-page-box__title"
    )
    EXTEND_SUBSCRIPTION_NOTIFICATION = by.css(".notification-message__owner")
    EXTEND_LINK_ON_NOTIFICATION = by.css(".notification-message__owner a")

    # COMPANY PROFILE WIDGET
    COMPANY_NAME = by.xpath('//*[@class="q-page-box company-information"]/div[2]/div[1]/h3')
    ESTABLISHMENT_NUMBER = by.xpath(
        '//*[@class="q-page-box company-information"]/div[2]/div[1]/dl/div[1]/dd'
    )
    ESTABLISHMENT_STATUS = by.xpath(
        '//*[@class="q-page-box company-information"]/div[2]/div[1]/dl/div[2]/dd'
    )
    UNIFIED_NATIONAL_NUMBER = by.xpath(
        '//*[@class="q-page-box company-information"]/div[2]/div[1]/dl/div[6]/dd'
    )

    links = {
        "About us": by.css(".q-footer__links > ul:nth-child(2) a"),
        "Labor market index": by.css(".q-footer__links > ul:nth-child(4) > li:nth-child(1)"),
        "Labor Policies": by.css(".q-footer__links > ul:nth-child(4) > li:nth-child(2)"),
        "Knowledge Center": by.css(".q-footer__links > ul:nth-child(4) > li:nth-child(3)"),
        "HRSD": by.css(".q-footer__logos li:nth-child(2) img"),
        "Takamol holding": by.css(".q-footer__logos li:nth-child(1) img"),
    }


class DashboardPage(DashboardLocators):
    def __init__(self):
        super().__init__()
        self.page_url = "/en/company"

    def click_on_switch_account_link(self):
        s(self.SWITCH_ACCOUNT_LINK).should(be.clickable).click()
        return self

    def select_e_services_menu_item(self):
        s(self.E_SERVICES_MENU).click()
        return self

    def select_control_panel_element(self):
        s(self.CONTROL_PANEL).should(be.visible).click()
        s(self.COMPANY_NAMES_LIST).wait_until(be.visible)
