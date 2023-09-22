from selene import have
from selene.support.shared.jquery_style import s


class PrivacyPolicyPage:
    TITLE = s("div.privacy-policy-info > h1")
    GEN_INFO_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[1]')
    READ_PARAGRAPH_TITLE = s('(//div[@class="privacy-policy-info"]/h3)[1]')
    READ_PARAGRAPH_TEXT = s('(//div[@class="privacy-policy-info"]/p)[1]')
    INFO_GIVE_PARAGRAPH_TITLE = s('(//div[@class="privacy-policy-info"]/h3)[2]')
    INFO_GIVE_PARAGRAPH_TEXT = s('(//div[@class="privacy-policy-info"]/p)[2]')
    INFO_COLLECT_PARAGRAPH_TITLE = s('(//div[@class="privacy-policy-info"]/h3)[3]')
    INFO_COLLECT_PARAGRAPH_TEXT = s('(//div[@class="privacy-policy-info"]/p)[3]')
    INFO_COLLECT_PARAGRAPH_LIST = s('(//div[@class="privacy-policy-info"]/ul)[1]')
    INFO_RECEIVE_PARAGRAPH_TITLE = s('(//div[@class="privacy-policy-info"]/h3)[4]')
    INFO_RECEIVE_PARAGRAPH_TEXT = s('(//div[@class="privacy-policy-info"]/p)[4]')

    DETAILS_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[2]')
    COOKIES_TITLE = s('(//div[@class="privacy-policy-info"]/h3)[5]')
    COOKIES_PARAGRAPH_1 = s('(//div[@class="privacy-policy-info"]/p)[5]')
    USE_COOKIES_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[3]')
    USE_COOKIES_LIST = s('(//div[@class="privacy-policy-info"]/ul)[2]')
    COOKIES_PARAGRAPH_2 = s('(//div[@class="privacy-policy-info"]/p)[6]')
    COOKIES_PARAGRAPH_3 = s('(//div[@class="privacy-policy-info"]/p)[7]')

    USES_MADE_OF_INFO_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[4]')
    USES_MADE_OF_INFO_PARAGRAPH = s('(//div[@class="privacy-policy-info"]/p)[8]')
    USES_MADE_OF_INFO_LIST = s('(//div[@class="privacy-policy-info"]/ul)[3]')

    INFO_RECEIVE_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[5]')
    INFO_RECEIVE_PARAGRAPH = s('(//div[@class="privacy-policy-info"]/p)[9]')

    DISCLOSURE_INFO_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[6]')
    DISCLOSURE_INFO_PARAGRAPH = s('(//div[@class="privacy-policy-info"]/p)[10]')
    DISCLOSURE_INFO_LIST = s('(//div[@class="privacy-policy-info"]/ul)[4]')

    CONSENT_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[7]')
    CONSENT_PARAGRAPH_1 = s('(//div[@class="privacy-policy-info"]/p)[11]')
    CONSENT_PARAGRAPH_2 = s('(//div[@class="privacy-policy-info"]/p)[12]')
    CONSENT_PARAGRAPH_3 = s('(//div[@class="privacy-policy-info"]/p)[13]')
    CONSENT_PARAGRAPH_4 = s('(//div[@class="privacy-policy-info"]/p)[14]')

    YOUR_RIGHTS_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[8]')
    YOUR_RIGHTS_PARAGRAPH_1 = s('(//div[@class="privacy-policy-info"]/p)[15]')
    YOUR_RIGHTS_PARAGRAPH_2 = s('(//div[@class="privacy-policy-info"]/p)[16]')

    CHANGES_TITLE = s('(//div[@class="privacy-policy-info"]/h2)[9]')
    CHANGES_PARAGRAPH_1 = s('(//div[@class="privacy-policy-info"]/p)[17]')
    CHANGES_PARAGRAPH_2 = s('(//div[@class="privacy-policy-info"]/p)[18]')

    @staticmethod
    def check_translation_with_xlsx_model(element, expected_value):
        assert element.should(have.exact_text(expected_value))
