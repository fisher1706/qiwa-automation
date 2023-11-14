from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User
from src.api.payloads.ibm.createnewcontract import (
    AddedClauseItem,
    AddedClauses,
    AdditionalAllowanceItem,
    AdditionalAllowancesList,
    AllowanceItem,
    Allowances,
    Body,
    ContractDetails,
    CreateNewContractRq,
    CreateNewContractRqPayload,
    EstablishmentDetails,
    ExpiryDate,
    JobTitle,
    LaborerDetails,
    LaborerDOB,
    OptionalArticles,
    RequesterDetails,
    StartDate,
)
from src.api.payloads.ibm.header import Header, UserInfo


def contract_details_payload(laborer: Laborer, employer: User, establishment_id: str) -> dict:
    return CreateNewContractRqPayload(
        CreateNewContractRq=CreateNewContractRq(
            Header=Header(
                TransactionId="1693833038",
                ChannelId="Qiwa",
                SessionId="212",
                RequestTime="2019-10-10 00:00:00.555",
                MWRequestTime="2019-10-10 00:00:00.555",
                ServiceCode="CNC00001",
                DebugFlag="1",
                UserInfo=UserInfo(IDNumber=laborer.login_id),
            ),
            Body=Body(
                EstablishmentDetails=EstablishmentDetails(
                    LaborOfficeId=employer.labor_office_id,
                    SequenceNumber=employer.sequence_number,
                    EstablishmentId=establishment_id,
                    UnifiedNumberId="10529",
                    EntityId="1-3419-460",
                    EstablishmentNameAr="Name",
                    EstablishmentNameEn="Name",
                    EstablishmentEmail="name@name",
                ),
                LaborerDetails=LaborerDetails(
                    LaborerIdNo=laborer.login_id,
                    LaborerName="jana",
                    LaborerTypeId="2",
                    LaborerIdExpiryDate="2022-10-10 00:00:00.555",
                    LaborerEmail="lab@lab",
                    LaborerMobileNumber="011111111",
                    DOBType="1",
                    LaborerDOB=LaborerDOB(HijriDate="14300530"),
                    EducationId="2",
                    SpecialtyId="2",
                    WorkLocationId="2",
                    IBAN="2",
                ),
                RequesterDetails=RequesterDetails(
                    RequesterIdNo="1032622902", RequesterName="name", RequesterUserId="525"
                ),
                ContractDetails=ContractDetails(
                    OccupationId="265202",
                    JobTitle=JobTitle(JobTitleAr="job", JobTitleEng="job"),
                    LaborerJobNumber="15",
                    ContractTypeId="1",
                    ContractDurationId="1",
                    ContractPeriod="12",
                    ProbationPeriod="90",
                    WorkingHoursTypeId="2",
                    VacationPeriod="21",
                    Salary="100000",
                    SalaryTypeId="1",
                    Allowances=Allowances(
                        AllowancesItems=[
                            AllowanceItem(Key="Allowance1", Value="2000"),
                            AllowanceItem(Key="Allowance2", Value="500"),
                        ]
                    ),
                    StartDate=StartDate(HijriDate="14420411", GregDate="2019-10-10 00:00:00.555"),
                    ExpiryDate=ExpiryDate(
                        HijriDate="14430411", GregDate="2020-10-10 00:00:00.555"
                    ),
                    RenewalStatusId="1",
                    NoticePeriod="30",
                    AddedClauses=AddedClauses(
                        AddedClausesItems=[
                            AddedClauseItem(Key="Clause1", Value="1"),
                            AddedClauseItem(Key="Clause2", Value="2"),
                        ]
                    ),
                    SalaryFrequency="1",
                    AdditionalAllowancesList=AdditionalAllowancesList(
                        Item=[
                            AdditionalAllowanceItem(
                                BenefitNameAr="benefit",
                                BenefitNameEn="benefit",
                                Frequency="1",
                                AmountType="1",
                                Amount="1000",
                            ),
                            AdditionalAllowanceItem(
                                BenefitNameAr="benefit2",
                                BenefitNameEn="benefit2",
                                Frequency="1",
                                AmountType="1",
                                Amount="2000",
                            ),
                        ]
                    ),
                    HoursPerWeek="40",
                    DaysPerWeek="5",
                    HoursPerDay="8",
                    OptionalArticles=OptionalArticles(
                        Period="3", Location="location", WorkField="field"
                    ),
                ),
                LanguageId="1",
                DateTypeId="2",
                RelatedToId=3,
            ),
        )
    ).dict()
