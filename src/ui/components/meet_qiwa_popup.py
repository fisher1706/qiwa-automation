from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s


class MeetQiwaPopup:
    popup = s("#modalBodyWrapper")
    close_icon = s('[aria-label="Close modal"]')

    @allure.step("Close Meet Qiwa popup")
    def close_meet_qiwa_popup(self) -> None:
        if self.popup.matching(be.visible) and self.popup.s("h2").matching(
            have.text("Meet Qiwa")
        ):
            self.close_icon.click()
