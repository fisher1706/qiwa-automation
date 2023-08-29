from pydantic import BaseModel


class DelegationMain(BaseModel):
    services_breadcrumb: str = "Services"
    delegation_main_page_breadcrumb: str = "Delegation to external entities"
    main_page: str = "Delegation Dashboard page"
    main_page_title: str = "Delegation to external entities"
    government_tab: str = "Government"
    add_delegation_button: str = "Add delegation"
    table_title: str = "Government delegations"
    filter_button: str = "Filters"
