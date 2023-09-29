import allure
import pytest

from data.lmi.constants import DimensionsInfo
from data.lmi.data_set import DimensionDataSet
from src.ui.lmi import lmi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check create dimension')
@case_id(17339, 17340, 17273)
def test_create_dimension(login_lmi_user):
    lmi.open_dimensions_weq_page()
    lmi.dimension_weq.create_new_dimension()


@allure.title('Check edit dimension')
@case_id(17269)
def test_edit_dimension(login_lmi_user):
    lmi.open_dimensions_weq_page()
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.dimension_weq.edit_dimension()


@allure.title('Check delete dimension')
@case_id(17267)
def test_delete_dimension(login_lmi_user):
    lmi.open_dimensions_weq_page()
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.dimension_weq.delete_dimension()


@allure.title('Check cancel delete dimension')
def test_cancel_edit_dimension(login_lmi_user):
    lmi.open_dimensions_weq_page()
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.dimension_weq.cancel_edit_dimension()


@allure.title('Check cancel edit dimension')
def test_cancel_delete_dimension(login_lmi_user):
    lmi.open_dimensions_weq_page()
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.dimension_weq.cancel_delete_dimension()


@allure.title('Check create already created dimension')
@pytest.mark.parametrize('name_en, name_ar, message', DimensionDataSet.dimension_created_names_value)
def test_create_already_created_dimension(login_lmi_user, name_en, name_ar, message):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.open_dimensions_weq_page()
    lmi.dimension_weq.create_already_created_dimension(name_en, name_ar, message)


@allure.title('Check create dimension with invalid values')
@case_id(17337, 17338, 17339, 17341, 11973, 11974)
@pytest.mark.parametrize('name_en, name_ar', DimensionDataSet.invalid_dimension_names_value)
def test_create_dimension_with_invalid_values(login_lmi_user, name_en, name_ar):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.open_dimensions_weq_page()
    lmi.dimension_weq.create_dimension_with_invalid_values(name_en, name_ar)


@allure.title('Check edit already created dimension')
@pytest.mark.parametrize('name_en, name_ar, message', DimensionDataSet.dimension_created_names_value)
def test_edit_already_created_dimension(login_lmi_user, name_en, name_ar, message):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE_EDIT, DimensionsInfo.NAME_AR_TEXT_EDIT,
                                                       lmi.cookie)
    lmi.open_dimensions_weq_page()
    lmi.dimension_weq.edit_already_created_dimension(name_en, name_ar, message)


@allure.title('Check edit dimension with invalid values')
@pytest.mark.parametrize('name_en, name_ar', DimensionDataSet.invalid_dimension_names_value)
def test_edit_dimension_with_invalid_values(login_lmi_user, name_en, name_ar):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT, lmi.cookie)
    lmi.open_dimensions_weq_page()
    lmi.dimension_weq.edit_dimension_with_invalid_values(name_en, name_ar)
