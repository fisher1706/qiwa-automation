from __future__ import annotations

import allure
from selene import be
from selene.support.shared.jquery_style import s


class MeetQiwaPopup:
    popup = s("#modalBodyWrapper")
    close_icon = s('[aria-label="Close modal"]')

    @allure.step
    def close_meet_qiwa_popup(self) -> None:
        if self.popup.matching(be.visible):
            self.close_icon.click()
