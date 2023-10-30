import allure
from selene import be
from selene.support.shared import browser

import config
from src.api.app import QiwaApi
from src.api.dataportal.workforcestatistics_api import workforce_api
from src.ui.pages.data_portal_pages.about_us_page import AboutUsPage
from src.ui.pages.data_portal_pages.all_sectors_page import AllSectorsPage
from src.ui.pages.data_portal_pages.contact_us_page import ContactUsPage
from src.ui.pages.data_portal_pages.data_portal_admin import DataPortalAdmin
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
        self.data_portal_admin = DataPortalAdmin()
        self.cookies = {}
        self.qiwa_api = QiwaApi()

    def wait_data_portal_page_to_load(self):
        self.footer.ACCEPT_COOKIES.click()
        self.footer.SPINNER.wait_until(be.not_.visible)

    @allure.step
    def open_privacy_policy(self):
        browser.open(f"{config.qiwa_urls.data_portal_url}/privacy-policy")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_home_page(self):
        browser.open(config.qiwa_urls.data_portal_url)
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_contact_us_page(self):
        browser.open(f"{config.qiwa_urls.data_portal_url}/contact-us")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_about_us_page(self):
        browser.open(f"{config.qiwa_urls.data_portal_url}/about-us")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_all_sectors_page(self):
        browser.open(f"{config.qiwa_urls.data_portal_url}/sectors")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_reports_page(self):
        browser.open(f"{config.qiwa_urls.data_portal_url}/reports")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_market_overview_page(self):
        workforce_api.get_bearer_token()
        workforce_api.get_max_date()
        browser.open(f"{config.qiwa_urls.data_portal_url}/market-overview")
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_nitaqat_activity_sector_page(self, sector_id):
        workforce_api.get_bearer_token()
        workforce_api.get_max_date()
        browser.open(
            f"{config.qiwa_urls.data_portal_url}/sector/?id={sector_id}&type=NITAQAT&colorIndex=4"
        )
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_economic_activity_sector_page(self, sector_id):
        workforce_api.get_bearer_token()
        workforce_api.get_max_date()
        browser.open(
            f"{config.qiwa_urls.data_portal_url}/sector/?chapter={sector_id}&type=ISIC&colorIndex=1"
        )
        self.wait_data_portal_page_to_load()
        return self

    @allure.step
    def open_data_portal_admin_login_page(self):
        browser.driver.delete_all_cookies()
        browser.open(config.qiwa_urls.data_portal_admin_url)
        return self

    @allure.step
    def open_data_portal_admin_category_page(self):
        browser.open(
            f"{config.qiwa_urls.data_portal_admin_url}/admin/structure/taxonomy/manage/category/overview"
        )
        return self

    @allure.step
    def open_data_portal_admin_report_page(self):
        browser.open(f"{config.qiwa_urls.data_portal_admin_url}/admin/content/reports")
        return self

    @allure.step
    def open_data_portal_admin_takeaway_page(self):
        browser.open(f"{config.qiwa_urls.data_portal_admin_url}/admin/content/takeaway-sections")
        return self

    @allure.step
    def open_data_portal_admin_content_page(self):
        browser.open(f"{config.qiwa_urls.data_portal_admin_url}/admin/content")
        return self

    def get_cookie(self):
        cookies = browser.driver.get_cookies()
        for cookie in cookies:
            if cookie["name"] == "SESS7c7d78a277693b7a3a692e8537bd44d3":
                self.cookies = f'{cookie["name"]}={cookie["value"]}'


data_portal = DataPortal()
