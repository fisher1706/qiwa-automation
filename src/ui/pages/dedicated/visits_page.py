from selene.support.shared.jquery_style import s


class VisitsPage:
    proceed_button = s('.btn.with-preloader')

    def click_on_proceed_button(self) -> None:
        self.proceed_button.click()
