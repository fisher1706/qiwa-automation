import allure

from src.ui.pages.spaces_page import SpacesPage


class SpacesActions(SpacesPage):
    @allure.step("Steps for create new space")
    def create_new_space(
        self,
        english_title,
        arabic_title,
        english_link,
        arabic_link,
        redirect_key_name,
        user_type,
        title,
    ):
        self.wait_page_to_load()
        self.go_to_add_space_page()
        self.check_create_space_page(title)
        self.fill_in_the_fields_for_new_space(
            english_title, arabic_title, english_link, arabic_link, redirect_key_name, user_type
        )
        self.click_on_create_space_button()

    @allure.step("Edit space english title")
    def edit_space(self, title, save=True):
        self.go_to_edit_space_page()
        self.enter_data_to_eng_name_field(title)
        if save:
            self.click_on_create_space_button()

    @allure.step("Deleting space")
    def delete_space(self):
        self.deleting()
