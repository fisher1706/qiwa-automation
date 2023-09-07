import allure
from selene import be
from selene.support.shared import browser

from src.api.dataportal.workforcestatistics_api import workforce_api
from src.ui.pages.data_portal_pages.about_us_page import AboutUsPage
from src.ui.pages.data_portal_pages.all_sectors_page import AllSectorsPage
from src.ui.pages.data_portal_pages.contact_us_page import ContactUsPage
from src.ui.pages.data_portal_pages.footer_block import FooterBlock
from src.ui.pages.data_portal_pages.header_block import HeaderBlock
from src.ui.pages.data_portal_pages.home_page import HomePage
from src.ui.pages.data_portal_pages.market_overview_page import MarketOverViewPage
from src.ui.pages.data_portal_pages.privacy_policy_page import PrivacyPolicyPage
from src.ui.pages.data_portal_pages.report_page import ReportsPage
from src.ui.pages.data_portal_pages.sector_page import SectorPage


class DataPortal:
    def __init__(self):
        super().__init__()
        self.about_us_page = AboutUsPage()
        self.privacy_policy = PrivacyPolicyPage()
        self.header = HeaderBlock()
        self.footer = FooterBlock()
        self.home_page = HomePage()
        self.contact_us_page = ContactUsPage()
        self.all_sectors_page = AllSectorsPage()
        self.market_overview_page = MarketOverViewPage()
        self.reports_page = ReportsPage()
        self.sector_page = SectorPage()

    def wait_data_portal_page_to_load(self):
        self.footer.ACCEPT_COOKIES.click()
        self.footer.SPINNER.wait_until(be.not_.visible)

    @allure.step
    def open_privacy_policy(self):
        browser.open("https://data.qiwa.info/privacy-policy")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_home_page(self):
        browser.open("https://data.qiwa.info/")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_contact_us_page(self):
        browser.open("https://data.qiwa.info/contact-us")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_about_us_page(self):
        browser.open("https://data.qiwa.info/about-us")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_all_sectors_page(self):
        browser.open("https://data.qiwa.info/sectors")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_reports_page(self):
        browser.open("https://data.qiwa.info/reports")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_market_overview_page(self):
        workforce_api.get_bearer_token()
        workforce_api.get_max_date()
        browser.open("https://data.qiwa.info/market-overview")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_nitaqat_activity_sector_page(self, sector_id):
        workforce_api.get_bearer_token()
        workforce_api.get_max_date()
        browser.open(f"https://data.qiwa.info/sector/?id={sector_id}&type=NITAQAT&colorIndex=4")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_economic_activity_sector_page(self, sector_id):
        workforce_api.get_bearer_token()
        workforce_api.get_max_date()
        browser.open(f"https://data.qiwa.info/sector/?chapter={sector_id}&type=ISIC&colorIndex=1")
        self.wait_data_portal_page_to_load()
        return self


data_portal = DataPortal()
