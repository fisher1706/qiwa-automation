import allure

from src.api.clients.lmi.dashboard_api import DashboardApi
from src.api.clients.lmi.survey_result_api import SurveyResultApi
from src.api.clients.lmi.weq_api import WeqApi


class WeqApiAction(WeqApi):
    def __init__(self, api):
        super().__init__(api)
        self.survey_result_api = SurveyResultApi(api)
        self.dashboard_api = DashboardApi(api)

    @allure.step("I perform calculation for overall_index and compare with current value")
    def perform_calculation(self, surveys_id, result_xlsx):
        self.post_calculate_indexes()
        self.dashboard_api.get_surveys_detail(surveys_id)
        self.survey_result_api.get_download_xls_result(surveys_id, result_xlsx)
        self.survey_result_api.parse_excel_file(result_xlsx)
        self.get_list_for_calculation(
            self.dashboard_api.survey, self.survey_result_api.parse_xls_result
        )
        self.handle_dimensions(self.list_for_calculation)
        overall_index = round(sum(self.d_value_lists), 2)
        self.get_total_final_index()
        assert overall_index == self.total_final_index, (
            f"The calculated index:{overall_index}"
            f" not matched with actual:{self.total_final_index}"
        )
