from selene import be, query
from selene.support.shared.jquery_style import s

from data.constants import Language


class Languages:
    lang_buttons = {
        Language.EN: '//button[contains(., "English")]',
        Language.AR: '//button[contains(., "العربية")]',
    }

    def click_on_lang_button(self, lang_value):
        button = s(self.lang_buttons[lang_value]).should(be.visible)
        button_state = button.get(query.attribute("disabled"))
        if not button_state:
            button.click()
