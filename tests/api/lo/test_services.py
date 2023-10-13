import allure

from data.lo.constants import LOSysAdmin, RequesterTypeId, ServicesInfo
from src.api.app import QiwaApi


@allure.title('Get all exist services')
def test_services():
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.services_api_actions.get_services()


@allure.title('Create new service with Establishment Request type')
def test_create_service_with_establish(index_name="Create with establish"):
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.services_api_actions.create_service(RequesterTypeId.ESTABLISHMENT,
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_EN} {index_name}",
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_AR} {index_name}")


@allure.title('Create new service with Individuals Request type')
def test_create_service_with_individual(index_name="Create with individual"):
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.services_api_actions.create_service(RequesterTypeId.INDIVIDUAL,
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_EN} {index_name}",
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_AR} {index_name}")


@allure.title('Edit service')
def test_edit_service(index_name="Edit service"):
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.services_api_actions.create_service(RequesterTypeId.ESTABLISHMENT,
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_EN} {index_name}",
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_AR} {index_name}")
    qiwa.services_api_actions.edit_service(RequesterTypeId.ESTABLISHMENT,
                                           f"{ServicesInfo.SERVICE_RANDOM_NAME_EN} 'Edited'",
                                           f"{ServicesInfo.SERVICE_RANDOM_NAME_AR}'الآلي' ")


@allure.title('Edit sub service')
def test_edit_sub_service(index_name="Edit sub service"):
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.services_api_actions.create_service(RequesterTypeId.ESTABLISHMENT,
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_EN} {index_name}",
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_AR} {index_name}")
    qiwa.services_api_actions.edit_sub_service(RequesterTypeId.ESTABLISHMENT,
                                               f"{ServicesInfo.SERVICE_RANDOM_NAME_EN} 'Edited'",
                                               f"{ServicesInfo.SERVICE_RANDOM_NAME_AR}'الآلي' ")


@allure.title('Change service status')
def test_change_service_status(index_name="Change service status"):
    qiwa = QiwaApi.login_as_user(LOSysAdmin.ID)
    qiwa.services_api_actions.create_service(RequesterTypeId.ESTABLISHMENT,
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_EN} {index_name}",
                                             f"{ServicesInfo.SERVICE_RANDOM_NAME_AR} {index_name}")
    qiwa.services_api_actions.change_status_service(RequesterTypeId.ESTABLISHMENT,
                                                    ServicesInfo.SERVICE_RANDOM_NAME_EN,
                                                    ServicesInfo.SERVICE_RANDOM_NAME_AR)
