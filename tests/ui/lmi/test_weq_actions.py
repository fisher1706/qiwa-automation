import allure
import pytest

from data.lmi.constants import DimensionsInfo
from src.ui.lmi import lmi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Test calculation')
@case_id(11995, 17327, 17328, 17329)
@pytest.mark.skip("Skipped due to https://employeesgate.atlassian.net/browse/LR-2343")
def test_calculation(login_lmi_user):
    lmi.qiwa_api.dimensions_api.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.retail_sector_weq.recalculation_overall_index()
    lmi.qiwa_api.get_total_final_index(lmi.cookie)
    lmi.retail_sector_weq.check_overall_index(lmi.wei_api.total_final_index)


@allure.title('Test Publish Result')
@case_id(17330)
@pytest.mark.skip("Skipped due to https://employeesgate.atlassian.net/browse/LR-2343")
def test_publishing_result(login_lmi_user):
    lmi.test_calculation()
    lmi.retail_sector_weq.publishing_result()
    lmi.lmi_landing.get_retail_indexes_value(lmi.retail_sector_weq.overall_index)
