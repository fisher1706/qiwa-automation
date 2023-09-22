import allure
import jmespath

from data.lmi.constants import Actions
from src.api.clients.lmi.survey_result_api import SurveyResultApi


class SurveyResultApiAction(SurveyResultApi):
    @allure.step("Create new link")
    def create_new_link(self, survey_id, link_name):
        self.post_link(survey_id, link_name)
        actual_name = jmespath.search("data.attributes.name", self.link_details)
        assert actual_name == link_name, f"Setup name: {link_name} \n Actual name: {actual_name}"

    @allure.step("Edit link")
    def edit_link(self, survey_id, link_name):
        link_name_edited = f"{link_name} edited"
        self.patch_link(self.link_id, link_name_edited)
        self.get_link(survey_id, self.link_id)
        actual_name = jmespath.search("data[0].attributes.name", self.link_details)
        assert (
            actual_name == link_name_edited
        ), f"Setup name: {link_name_edited} \n Actual name: {actual_name}"

    @allure.step("Delete link")
    def delete_link(self, survey_id, *_):
        self.del_link(self.link_id)
        self.get_link(survey_id, self.link_id)
        link_id = jmespath.search("data[0].id", self.link_details)
        assert link_id is None, f"Link isn't deleted and has id: {link_id}"

    @allure.step("Link views amount")
    def check_link_views(self, survey_id, *_):
        current_views = jmespath.search("data.attributes.number_of_clicks", self.link_details)
        link_hex = jmespath.search("data.attributes.link", self.link_details).split("=")[1]
        self.post_company_name(link_hex)
        self.get_link(survey_id, self.link_id)
        actual_views = jmespath.search("data[0].attributes.number_of_clicks", self.link_details)
        assert actual_views == current_views + 1, (
            f"Incorrect works link counter:\n Expect views amount={current_views + 1}\n"
            f"Actual views amount={actual_views}"
        )

    def define_action(self, action, *arg):
        actions_dict = {
            Actions.EDIT: self.edit_link,
            Actions.DELETE: self.delete_link,
            Actions.COUNTER: self.check_link_views,
        }
        if action in actions_dict:
            actions_dict[action](*arg)
