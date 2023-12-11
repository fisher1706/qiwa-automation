import allure

from data.lmi.constants import Actions
from src.api.clients.lmi.dashboard_api import DashboardApi
from src.api.clients.lmi.dimensions_api import DimensionsApi


class DimensionsApiAction(DimensionsApi):
    def __init__(self, api):
        super().__init__(api)
        self.dashboard_api = DashboardApi(api)

    @allure.step("I create dimension")
    def create_dimension(self, name_en, name_ar, name_en_validation):
        self.post_dimension(name_en, name_ar)
        self.get_last_dimension_id()
        self.get_dimension(self.last_dimension_id)
        assert self.dimension["data"]["attributes"]["name"] == name_en_validation
        assert self.dimension["data"]["attributes"]["ar_name"] == name_ar

    @allure.step("I delete dimension for particular survey")
    def delete_dimension(self, *_):
        self.del_dimension(self.last_dimension_id)
        assert self.get_dimension(self.last_dimension_id, expect_code=400, expect_schema=None)

    @allure.step("I edit names of dimension")
    def edit_dimension_names(self, name_en_edited, name_ar_edited, name_en_edited_validation):
        self.put_dimension_names(name_en_edited, name_ar_edited, self.last_dimension_id)
        self.get_dimension(self.last_dimension_id)
        assert self.dimension["data"]["attributes"]["name"] == name_en_edited_validation
        assert self.dimension["data"]["attributes"]["ar_name"] == name_ar_edited

    @allure.step("I attach question to dimension")
    def attach_questions(self, surveys_id, cookies=None):
        self.get_last_dimension_id(cookies)
        self.dashboard_api.get_surveys_detail(surveys_id, cookies)
        self.put_attach_question(self.last_dimension_id, self.dashboard_api.question_id, cookies)
        self.get_dimension(self.last_dimension_id, surveys_id, cookies)
        assert self.dashboard_api.question_id in self.dimension_questions_id

    @allure.step("I detach question from dimension")
    def detach_questions(self, surveys_id):
        self.put_detach_question(self.last_dimension_id, self.dashboard_api.question_id)
        self.get_dimension(self.last_dimension_id, surveys_id)
        assert self.dashboard_api.question_id not in self.dimension_questions_id

    def define_action(self, action, values):
        actions_dict = {
            Actions.EDIT: self.edit_dimension_names,
            Actions.DELETE: self.delete_dimension,
        }
        if action in actions_dict:
            actions_dict[action](*values)
