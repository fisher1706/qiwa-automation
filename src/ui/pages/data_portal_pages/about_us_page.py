from selene import have, query
from selene.support.shared.jquery_style import browser, s, ss

from data.dataportal.constants import Links


class AboutUsPage:
    HERO_TITLE = s('//div[@class="about-us-caption"]//h1')
    HERO_DESCRIPTION = s('//div[@class="about-us-caption"]//h2')

    MISSION_TITLE = s('//div[@class="our-mission"]//h2')
    MISSION_CARD_ICON = s('//div[@class="our-mission"]//img')
    MISSION_CARD_TITLE = ss('//div[@class="our-mission"]//h3')
    MISSION_CARD_DESCRIPTION = ss('//div[@class="our-mission"]//p')

    BENEFITS_TITLE = s('//div[@class="our-benefits"]//h2')
    BENEFITS_CARD_ICON = s('//div[@class="our-benefits"]//img')
    BENEFITS_CARD_TITLE = ss('//div[@class="our-benefits"]//h3')
    BENEFITS_CARD_DESCRIPTION = ss('//div[@class="our-benefits"]//p')

    BELIEVE_TITLE = s('//div[@class="believe-block"]//h2')
    BELIEVE_CARD_ICON = s('//div[@class="believe-block"]//img')
    BELIEVE_CARD_TITLE = ss('//div[@class="believe-block"]//h3')
    BELIEVE_CARD_DESCRIPTION = ss('//div[@class="believe-block"]//p')

    QIWA_SA_TITLE = s('//div[@class="first-column"]//a[@href]')
    QIWA_SA_DESCRIPTION = ss('//div[@class="information-block"]//p')
    QIWA_VISIT_TITLE = s('//div[@class="second-column"]//h3')
    QIWA_VISIT_LINK = ss(
        '//div[@class="body-02-short md-body-large-short social-links_item--title"]'
    )
    QIWA_VISIT_RESOURCE = s('//div[@class="second-column"]//a[@href]')

    TWITTER_SOCIAL_MEDIA = s('(//a[@href="https://twitter.com/qiwa_sa"])[2]')
    LINKEDIN_SOCIAL_MEDIA = s('(//a[@href="https://www.linkedin.com/company/qiwa-sa/"])[2]')

    def check_redirection_to_qiwa_sa_service_from_title(self):
        self.QIWA_SA_TITLE.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.QIWA_SA

    def check_redirection_to_qiwa_sa(self):
        self.QIWA_VISIT_RESOURCE.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.QIWA_SA

    def check_redirection_to_linkedin(self):
        self.LINKEDIN_SOCIAL_MEDIA.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.LINKEDIN

    def check_redirection_to_twitter(self):
        self.TWITTER_SOCIAL_MEDIA.click()
        browser.switch_to_next_tab()
        assert browser.driver.current_url == Links.TWITTER

    @staticmethod
    def check_element_on_the_page(element, text):
        element.should(have.text(text))

    @staticmethod
    def check_elements_on_the_page(elements, list_text):
        elements_list = []
        for element in elements:
            elements_list.append(element.get(query.text))
        assert elements_list == list_text, f"{elements_list}\n{list_text}"
