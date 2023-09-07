import dataclasses


@dataclasses.dataclass
class WorkForceStatistics:
    NUMBEROFESTABLISHMENTS = (
        "WFSResponse.response.fact.item[*].item[?name=='NUMBEROFESTABLISHMENTS'].value"
    )
    NOOFEMPLOYEES = "WFSResponse.response.fact.item[*].item[?name=='NOOFEMPLOYEES'].value"
    NOOFEMPLOYEE = "WFSResponse.response.fact.item[].item[].item[].item[].item[].value"
    NOOFUNIFIEDCOMPANIES = (
        "WFSResponse.response.fact.item[*].item[?name=='NOOFUNIFIEDCOMPANIES'].value"
    )
    NUMBEROFENTITIES = "WFSResponse.response.fact.item[*].item[?name=='NUMBEROFENTITIES'].value"

    TOTAL_EMPLOYEES = "WFSResponse.response.fact.item[*].item[?value=='TOTAL'].item[*].value"
    TOTAL_MALE = "WFSResponse.response.fact.item[*].item[?value=='Male'].item[*].value"
    TOTAL_FEMALE = "WFSResponse.response.fact.item[*].item[?value=='Female'].item[*].value"
    TOTAL_ESTABLISHMENTS = (
        "WFSResponse.response.fact.item[*].item[*].item[*].item[?name=='NOOFESTABLISHMENT'].value"
    )
    TOTAL_UNIFIED_COMPANIES = (
        "WFSResponse.response.fact.item[*].item[*].item[*].item[*]"
        ".item[?name=='NOOFUNIFIEDCOMPANIES'].value"
    )
    TOTAL_ENTITIES = "WFSResponse.response.fact.item[*].item[*].item[*].item[*].item[?name=='NOOFENTITIES'].value"
