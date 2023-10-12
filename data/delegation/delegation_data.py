from dataclasses import dataclass


@dataclass
class AllDelegations:
    def __init__(self, data: dict):
        self.total_elements = data["totalElements"]
        self.first_delegation_data = data["content"][0]
        self.first_delegation_id = data["content"][0]["id"]
        self.first_delegation_available_for_resending = data["content"][0]["availableForResending"]
        self.first_delegation_employee_name = data["content"][0]["employeeName"]
        self.first_delegation_entity_name_en = data["content"][0]["entityNameEn"]
        self.first_delegation_permission = data["content"][0]["permissions"][0]["nameEn"]
        self.first_delegation_status = data["content"][0]["status"]
        self.first_delegation_start_date = data["content"][0]["startDate"]
        self.first_delegation_expiry_date = data["content"][0]["expireAt"]


@dataclass
class DelegationDetails:
    def __init__(self, data: dict):
        self.partner_list = data["delegationApproveRequests"]
        self.delegate_name = data["employeeName"]
        self.delegate_nid = data["employeeNid"]
        self.delegate_nationality = data["employeeNationalityEn"]
        self.delegate_occupation = data["employeeJob"]
        self.delegation_status = data["status"]
        self.delegation_id = data["id"]
        self.entity_name_en = data["entityNameEn"]
        self.permission = data["permissions"][0]["nameEn"]
        self.start_date = data["startDate"]
        self.expiry_date = data["expireAt"]
