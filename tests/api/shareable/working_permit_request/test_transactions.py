from http import HTTPStatus

from src.api import models
from src.api.app import QiwaApi
from src.api.assertions.model import validate_model
from src.api.constants.work_permit import WorkPermitStatus
from src.api.controllers.ibm import IBMApiController
from src.api.models.ibm.getworkpermitrequests import IBMWorkPermitRequestList


def test_get_transactions(user, establishment):
    qiwa = QiwaApi.login_as_user(user).select_company()
    ibm_api = IBMApiController()

    payload = src.api.models.ibm.payloads.GetWorkPermitRequestsRq(
        LaborOfficeId=establishment.labor_office_id,
        SequenceNumber=establishment.sequence_number
    )
    ibm_data: IBMWorkPermitRequestList = ibm_api.get_work_permit_requests_from_ibm(payload)

    response = qiwa.wp_request_api.get_wp_transactions(expect_code=HTTPStatus.OK)
    response_json = response.json()

    validate_model(response_json, models.qiwa.work_permit.work_permit_requests_list)
    qiwa.wp_request_api.assert_transactions(response_json, ibm_data)


def test_get_transactions_by_status(user, establishment):
    qiwa = QiwaApi.login_as_user(user).select_company()
    ibm_api = IBMApiController()

    payload = src.api.models.ibm.payloads.GetWorkPermitRequestsRq(
        LaborOfficeId=establishment.labor_office_id,
        SequenceNumber=establishment.sequence_number,
        StatusId=WorkPermitStatus.PRINTED
    )
    ibm_data: IBMWorkPermitRequestList = ibm_api.get_work_permit_requests_from_ibm(payload)

    response = qiwa.wp_request_api.get_wp_transactions(status=WorkPermitStatus.PRINTED, expect_code=HTTPStatus.OK)
    response_json = response.json()

    validate_model(response_json, models.qiwa.work_permit.work_permit_requests_list)
    qiwa.wp_request_api.assert_transactions(response_json, ibm_data)
