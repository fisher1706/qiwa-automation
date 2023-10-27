from __future__ import annotations

from selene import be, have
from selene.support.shared.jquery_style import s, ss


class UserDetailsPage:
    user_details_title = s("//div[contains(@data-testid, 'section-header')]/div/p")
    subscribed_user_info = s("//div[contains(@data-testid, 'about-user-block')]//p[2]")
    subscribed_user_field_names = ss("//div[contains(@data-testid, 'about-user-block')]//p[1]")
    subscribed_user_name = subscribed_user_info.s("//div[1]/div[1]/p[2]")
    subscription_expiry_date = subscribed_user_info.s("//div[2]/div[2]/p[2]")
    subscribed_personal_number = subscribed_user_info.s("//div[1]/div[2]/p[2]")
    subscription_period_year = subscribed_user_info.s("//div[2]/div[1]/p[2]")

    full_name = subscribed_user_field_names[0]
    national_id = subscribed_user_field_names[1]
    subscription_period = subscribed_user_field_names[2]
    subscription_expiry_field = subscribed_user_field_names[3]

    terminate_btn = s("[data-testid='remove-user-block'] span")
    terminate_text = s("[data-testid='remove-user-block'] p")

    establishment_table_title = s("//div[contains(@data-testid, 'section-table')]/div/p[1]")
    establishment_table_text = s("//div[contains(@data-testid, 'section-table')]/div/p[2]")
    search_title = s("[role='search'] label")
    allowed_access_btn = s("//button[1]/div/p")
    no_access_btn = s("//button[2]/div/p")
    establishment_name_column = s("//thead/tr/th[2]")
    establishment_id_column = s("//thead/tr/th[3]")
    privileges_column = s("//thead/tr/th[4]")
    actions_column = s("//thead/tr/th[5]")
    details_page_breadcrumbs = s("[aria-label='Breadcrumb'] p")

    def check_user_details_title(self, title) -> UserDetailsPage:
        self.user_details_title.should(have.text(title))
        return self

    def check_users_info_block(self) -> UserDetailsPage:
        self.subscribed_user_name.should(be.visible)
        self.subscription_expiry_date.should(be.visible)
        self.subscribed_personal_number.should(be.visible)
        self.subscription_period_year.should(be.visible)
        return self

    def check_companies_table_is_displayed(self) -> UserDetailsPage:
        self.subscribed_user_info.should(be.visible)
        return self

    def check_ar_localization(self, *texts) -> UserDetailsPage:
        elements = [
            self.full_name,
            self.national_id,
            self.subscription_period,
            self.subscription_expiry_field,
            self.terminate_btn,
            self.terminate_text,
            self.establishment_table_title,
            self.establishment_table_text,
            self.search_title,
            self.no_access_btn,
            self.establishment_name_column,
            self.establishment_id_column,
            self.privileges_column,
            self.actions_column,
            self.details_page_breadcrumbs,
        ]

        for element, text in zip(elements, texts):
            element.should(have.text(text))

        return self
