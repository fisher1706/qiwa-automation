from selene import have
from selene.support.shared.jquery_style import s


class UserDetailsLocators:
    USER_DETAILS_TITLE = "//div[contains(@data-testid, 'section-header')]/div/p"


class UserDetailsPage(UserDetailsLocators):
    def check_user_details_title(self, title):
        s(self.USER_DETAILS_TITLE).should(have.text(title))
