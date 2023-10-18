# pylint: disable=too-few-public-methods
from dataclasses import dataclass

from data.lo.constants import (
    BasePageInfo,
    LOAgent,
    LOSysAdmin,
    OfficesInfo,
    RequesterTypeId,
    ServiceIds,
    ServicesInfo,
    SubServiceIds,
    UserAnyRole,
    VisitInfo,
    VisitReason,
)


class VisitsDataSet:
    VISIT_DETAILS = "visit_details"
    CANCEL_VISIT = "cancel_visit"

    visit_action_name = (None, CANCEL_VISIT, VISIT_DETAILS)

    visits_api_test_data = [
        {
            "description": "LO Admin book visit & cancel after",
            "user_id": LOSysAdmin.ID,
            "booking_data": {
                "office_id": OfficesInfo.AUTO_TEST_OFFICE_ID,
                "service_id": ServiceIds.POLICIES_SERVICE_ID,
                "region_id": OfficesInfo.NAJRAN_REGION_ID,
                "labor_office_id": LOSysAdmin.LABOR_OFFICE_ID,
                "sequence_number": LOSysAdmin.SEQUENCE_NUMBER,
                "sub_service_id": SubServiceIds.SUBMIT_POLICIES_REQUEST,
                "requester_type_id": RequesterTypeId.ESTABLISHMENT,
                "visit_reason_id": VisitReason.REQUEST_NEW_SERVICE_API,
                "timedelta": 1,
            },
        },
        {
            "description": "LO Agent book visit & cancel after",
            "user_id": LOAgent.ID,
            "booking_data": {
                "office_id": OfficesInfo.AUTO_TEST_OFFICE_ID,
                "service_id": ServiceIds.POLICIES_SERVICE_ID,
                "region_id": OfficesInfo.NAJRAN_REGION_ID,
                "labor_office_id": LOAgent.LABOR_OFFICE_ID,
                "sequence_number": LOAgent.SEQUENCE_NUMBER,
                "sub_service_id": SubServiceIds.SUBMIT_POLICIES_REQUEST,
                "requester_type_id": RequesterTypeId.ESTABLISHMENT,
                "visit_reason_id": VisitReason.REQUEST_NEW_SERVICE_API,
                "timedelta": 1,
            },
        },
        {
            "description": "Any user book visit & cancel after",
            "user_id": UserAnyRole.ID,
            "booking_data": {
                "office_id": OfficesInfo.AUTO_TEST_OFFICE_ID,
                "service_id": ServiceIds.POLICIES_SERVICE_ID,
                "region_id": OfficesInfo.NAJRAN_REGION_ID,
                "labor_office_id": UserAnyRole.LABOR_OFFICE_ID,
                "sequence_number": UserAnyRole.SEQUENCE_NUMBER,
                "sub_service_id": SubServiceIds.SUBMIT_POLICIES_REQUEST,
                "requester_type_id": RequesterTypeId.ESTABLISHMENT,
                "visit_reason_id": VisitReason.REQUEST_NEW_SERVICE_API,
                "timedelta": 1,
            },
        },
    ]

    visits_api_edit_test_data = [
        {
            "description": "LO Admin edit visit",
            "user_id": LOSysAdmin.ID,
            "booking_data": {
                "office_id": OfficesInfo.AUTO_TEST_OFFICE_ID,
                "service_id": ServiceIds.POLICIES_SERVICE_ID,
                "region_id": OfficesInfo.NAJRAN_REGION_ID,
                "labor_office_id": LOSysAdmin.LABOR_OFFICE_ID,
                "sequence_number": LOSysAdmin.SEQUENCE_NUMBER,
                "sub_service_id": SubServiceIds.SUBMIT_POLICIES_REQUEST,
                "requester_type_id": RequesterTypeId.ESTABLISHMENT,
                "visit_reason_id": VisitReason.REQUEST_NEW_SERVICE_API,
                "timedelta": 1,
            },
            "booking_data_edit": {
                "office_id": OfficesInfo.AUTO_TEST_OFFICE_ID,
                "service_id": ServiceIds.CHANGE_OCCUPATION_ID,
                "region_id": OfficesInfo.NAJRAN_REGION_ID,
                "labor_office_id": LOSysAdmin.LABOR_OFFICE_ID_EDIT,
                "sequence_number": LOSysAdmin.SEQUENCE_NUMBER_EDIT,
                "sub_service_id": SubServiceIds.SUBMIT_CHANGE_OCCUPATION,
                "requester_type_id": RequesterTypeId.ESTABLISHMENT,
                "timedelta": 1,
            },
        },
        # TODO investigate validation error
        # {
        #     'description': 'LO Agent edit visit',
        #     'user_id': LOAgent.ID,
        #     'booking_data': {
        #         'office_id': OfficesInfo.AUTO_TEST_OFFICE_ID,
        #         'service_id': ServiceIds.POLICIES_SERVICE_ID,
        #         'region_id': OfficesInfo.NAJRAN_REGION_ID,
        #         'labor_office_id': LOAgent.LABOR_OFFICE_ID,
        #         'sequence_number': LOAgent.SEQUENCE_NUMBER,
        #         'sub_service_id': SubServiceIds.SUBMIT_POLICIES_REQUEST,
        #         'requester_type_id': RequesterTypeId.ESTABLISHMENT,
        #         'visit_reason_id': VisitReason.REQUEST_NEW_SERVICE_API,
        #         'timedelta': 1
        #     },
        #     'booking_data_edit': {
        #         'office_id': OfficesInfo.AUTO_TEST_OFFICE_ID,
        #         'service_id': ServiceIds.CHANGE_OCCUPATION_ID,
        #         'region_id': OfficesInfo.NAJRAN_REGION_ID,
        #         'labor_office_id': LOAgent.LABOR_OFFICE_ID_EDIT,
        #         'sequence_number': LOAgent.SEQUENCE_NUMBER_EDIT,
        #         'sub_service_id': SubServiceIds.SUBMIT_CHANGE_OCCUPATION,
        #         'requester_type_id': RequesterTypeId.ESTABLISHMENT,
        #         'timedelta': 1
        #     }
        # },
        # {
        #     'description': 'Any user edit visit',
        #     'user_id': UserAnyRole.ID,
        #     'booking_data': {
        #         'office_id': OfficesInfo.AUTO_TEST_OFFICE_ID,
        #         'service_id': ServiceIds.POLICIES_SERVICE_ID,
        #         'region_id': OfficesInfo.NAJRAN_REGION_ID,
        #         'labor_office_id': UserAnyRole.LABOR_OFFICE_ID,
        #         'sequence_number': UserAnyRole.SEQUENCE_NUMBER,
        #         'sub_service_id': SubServiceIds.SUBMIT_POLICIES_REQUEST,
        #         'requester_type_id': RequesterTypeId.ESTABLISHMENT,
        #         'visit_reason_id': VisitReason.REQUEST_NEW_SERVICE_API,
        #         'timedelta': 1
        #     },
        #     'booking_data_edit': {
        #         'office_id': OfficesInfo.AUTO_TEST_OFFICE_ID,
        #         'service_id': ServiceIds.CHANGE_OCCUPATION_ID,
        #         'region_id': OfficesInfo.NAJRAN_REGION_ID,
        #         'labor_office_id': UserAnyRole.LABOR_OFFICE_ID,
        #         'sequence_number': UserAnyRole.SEQUENCE_NUMBER,
        #         'sub_service_id': SubServiceIds.SUBMIT_CHANGE_OCCUPATION,
        #         'requester_type_id': RequesterTypeId.ESTABLISHMENT,
        #         'timedelta': 1
        #     }
        # }
    ]

    user_role_ids_data = [
        (
            LOSysAdmin.ID,
            LOSysAdmin.LABOR_OFFICE_ID,
            LOSysAdmin.SEQUENCE_NUMBER,
            LOSysAdmin.LABOR_OFFICE_ID_EDIT,
            LOSysAdmin.SEQUENCE_NUMBER_EDIT,
        ),
        (
            LOAgent.ID,
            LOAgent.LABOR_OFFICE_ID,
            LOAgent.SEQUENCE_NUMBER,
            LOAgent.LABOR_OFFICE_ID_EDIT,
            LOAgent.SEQUENCE_NUMBER_EDIT,
        ),
        (
            UserAnyRole.ID,
            UserAnyRole.LABOR_OFFICE_ID,
            UserAnyRole.SEQUENCE_NUMBER,
            UserAnyRole.LABOR_OFFICE_ID_EDIT,
            UserAnyRole.SEQUENCE_NUMBER_EDIT,
        ),
    ]

    individual_scope_api = (
        OfficesInfo.INDIVIDUAL_OFFICE_ID,
        ServiceIds.INDIVIDUAL_SERVICE_ID,
        OfficesInfo.TABUK_REGION_ID,
        SubServiceIds.INDIVIDUAL_SUB_SERVICE_ID,
        RequesterTypeId.INDIVIDUAL,
    )

    individual_edit_scope_api = (
        OfficesInfo.INDIVIDUAL_OFFICE_ID,
        ServiceIds.INDIVIDUAL_SERVICE_ID,
        OfficesInfo.TABUK_REGION_ID,
        SubServiceIds.INDIVIDUAL_SUB_SERVICE_ID_2,
        RequesterTypeId.INDIVIDUAL,
    )

    visits_data_api = (
        (
            OfficesInfo.AUTO_TEST_OFFICE_ID,
            ServiceIds.POLICIES_SERVICE_ID,
            OfficesInfo.NAJRAN_REGION_ID,
            SubServiceIds.SUBMIT_POLICIES_REQUEST,
            RequesterTypeId.ESTABLISHMENT,
        ),
        individual_scope_api,
    )

    visits_edit_data_api = (
        (
            OfficesInfo.AUTO_TEST_OFFICE_ID,
            ServiceIds.CHANGE_OCCUPATION_ID,
            OfficesInfo.NAJRAN_REGION_ID,
            SubServiceIds.SUBMIT_CHANGE_OCCUPATION,
            RequesterTypeId.ESTABLISHMENT,
        ),
        individual_edit_scope_api,
    )

    individual_scope_ui = (
        VisitReason.REQUEST_NEW_SERVICE,
        BasePageInfo.INDIVID_REQUEST_TYPE,
        OfficesInfo.REGION_TABUK,
        OfficesInfo.INDIVIDUAL_OFFICE,
        ServicesInfo.INDIVIDUAL_SERVICE,
        ServicesInfo.INDIVIDUAL_SUB_SERVICE,
        VisitInfo.VISIT_CONFIRMED_MESSAGE,
    )

    individual_edit_scope_ui = (
        BasePageInfo.INDIVID_REQUEST_TYPE,
        ServicesInfo.INDIVIDUAL_SERVICE,
        ServicesInfo.INDIVIDUAL_SUB_SERVICE_2,
        VisitInfo.VISIT_EDITED_MESSAGE,
    )

    visit_data_ui = [
        (
            VisitReason.REQUEST_NEW_SERVICE,
            BasePageInfo.ESTABLISH_REQUEST_TYPE,
            OfficesInfo.REGION_NAJRAN,
            OfficesInfo.AUTO_TEST_OFFICE,
            ServicesInfo.POLICIES_SERVICE,
            ServicesInfo.POLICIES_SUB_SERVICE,
            VisitInfo.VISIT_CONFIRMED_MESSAGE,
        )
    ]

    visit_edit_data_ui = (
        (
            BasePageInfo.ESTABLISH_REQUEST_TYPE,
            ServicesInfo.POLICIES_SERVICE,
            ServicesInfo.POLICIES_SUB_SERVICE,
            VisitInfo.VISIT_EDITED_MESSAGE,
        ),
        individual_edit_scope_ui,
    )


@dataclass
class Case22173ServiceList:
    WORK_PERMIT = 4
    VISA = 6
    EMPLOYEE_TRANSFER = 3
    SC = 1
    CO = 2
    POLICY = 14
