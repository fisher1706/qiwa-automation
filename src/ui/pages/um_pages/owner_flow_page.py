from selene import have
from selene.support.shared.jquery_style import s


class OwnerFlowLocators:
    TITLES = ".ffQsyv"
    PROCEED_WITH_SUBSCRIPTION_BTN = "div.exizz button.dbHICy"


class OwnerFLowPage(OwnerFlowLocators):
    def check_title(self, title):
        s(self.TITLES).should(have.text(title))

    def click_proceed_with_subscription_btn(self):
        s(self.PROCEED_WITH_SUBSCRIPTION_BTN).click()
