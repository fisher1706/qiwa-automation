import jmespath

from src.api.clients.lmi.dashboard_api import DashboardApi


class DashboardApiAction(DashboardApi):
    def setup_survey_attribute(self, survey_id, attribute_json, group=None):
        attribute_dict = jmespath.search("data.attributes", attribute_json)
        self.put_survey_attribute(survey_id, attribute_json)
        self.get_surveys_detail(survey_id)
        if group:
            sector_ids = [item["id"] for item in self.survey["data"]["attributes"]["sectors"]]
            sector_ids = "" if sector_ids == [] else sorted(sector_ids)
            assert sector_ids == attribute_dict["sector_ids"]
        else:
            for key, value in self.survey["data"]["attributes"].items():
                if {key: value} == attribute_dict:
                    return
