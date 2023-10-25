from selene.support.shared.jquery_style import browser, s, ss

from data.data_portal.constants import Links


class FooterBlock:
    ACCEPT_COOKIES = s('(//div[@class="cookies-header"]//button)[2]')
    YOUTUBE_COOKIE_BUTTON = s('(//button[@jsname="b3VHJd"]//span[@class="VfPpkd-vQzf8d"])[1]')
    SPINNER = s('//div[@class="spinner"]')

    QIWA_LOGO = s('//footer//a[@class="logo-image"]/img')
    QIWA_SA_LINK_HERO = s('(//a[@href="https://qiwa.sa/"])[2]')
    SECTORS_TITLE = s('//div[@class="sectors-list-wrapper"]/div[1]')
    COMPANY_TITLE = s('//div[@class="company text-start"]/div[1]')

    TWITTER_SOCIAL_MEDIA = s('(//a[@href="https://twitter.com/qiwa_sa"])[2]')
    LINKEDIN_SOCIAL_MEDIA = s('(//a[@href="https://www.linkedin.com/company/qiwa-sa/"])[2]')
    YOUTUBE_SOCIAL_MEDIA = s('(//a[@href="https://www.youtube.com/qiwa_sa"])[2]')
    TAKAMOL = s('//a[@href="https://takamolholding.com/"]')
    HUMAN_RESOURCES = s('//a[@href="https://hrsd.gov.sa"]')

    VIEW_ALL_SECTORS = s('//div[@class="nav-link"]//a[@href="/sectors"]/span[1]')
    MARKET_OVERVIEW = s('//div[@class="nav-link"]//a[@href="/market-overview"]/span[1]')

    TERMS_OF_USER = s('//div[@class="links-list-bottom d-flex"]//a[1]')
    PRIVACY_POLICY = s('//div[@class="links-list-bottom d-flex"]//a[2]')

    ABOUT_US = s('(//div[@class="company text-start"]//a/span)[1]')
    CONTACT_US = s('(//div[@class="company text-start"]//a/span)[2]')

    SECTORS_ITEM = ss('//div[@class="items sector-item"]/a[@href]/span')

    def check_redirection_to_linkedin(self):
        self.LINKEDIN_SOCIAL_MEDIA.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.LINKEDIN

    def check_redirection_to_twitter(self):
        self.TWITTER_SOCIAL_MEDIA.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.TWITTER

    def check_redirection_to_youtube(self):
        self.YOUTUBE_SOCIAL_MEDIA.click()
        browser.switch_to_next_tab()
        self.YOUTUBE_COOKIE_BUTTON.click()
        assert browser.driver.current_url == Links.YOUTUBE

    def check_redirection_to_qiwa_sa(self):
        self.QIWA_SA_LINK_HERO.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.QIWA_SA

    def check_redirection_to_term_of_user(self):
        self.TERMS_OF_USER.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.TERMS_OF_USER

    def check_redirection_to_takamol(self):
        self.TAKAMOL.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.TAKAMOL

    def check_redirection_to_human_resources(self):
        self.HUMAN_RESOURCES.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.HUMAN_RESOURCES

    def check_navigation_to_all_sectors_page(self):
        self.VIEW_ALL_SECTORS.click()
        assert browser.driver.current_url == Links.VIEW_ALL_SECTORS

    def check_navigation_to_market_overview_page(self):
        self.MARKET_OVERVIEW.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    def check_navigation_to_privacy_policy_page(self):
        self.PRIVACY_POLICY.click()
        assert browser.driver.current_url == Links.PRIVACY_POLICY

    def check_navigation_to_about_us_page(self):
        self.ABOUT_US.click()
        assert browser.driver.current_url == Links.ABOUT_US

    def check_navigation_to_contact_us_page(self):
        self.CONTACT_US.click()
        assert browser.driver.current_url == Links.CONTACT_US
