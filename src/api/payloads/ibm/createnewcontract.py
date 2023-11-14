from pydantic import BaseModel

from src.api.payloads.ibm.header import Header


class EstablishmentDetails(BaseModel):
    LaborOfficeId: str
    SequenceNumber: str
    EstablishmentId: str
    UnifiedNumberId: str
    EntityId: str
    EstablishmentNameAr: str
    EstablishmentNameEn: str
    EstablishmentEmail: str


class LaborerDOB(BaseModel):
    HijriDate: str


class JobTitle(BaseModel):
    JobTitleAr: str
    JobTitleEng: str


class AllowanceItem(BaseModel):
    Key: str
    Value: str


class AddedClauseItem(BaseModel):
    Key: str
    Value: str


class AdditionalAllowanceItem(BaseModel):
    BenefitNameAr: str
    BenefitNameEn: str
    Frequency: str
    AmountType: str
    Amount: str


class LaborerDetails(BaseModel):
    LaborerIdNo: str
    LaborerName: str
    LaborerTypeId: str
    LaborerIdExpiryDate: str
    LaborerEmail: str
    LaborerMobileNumber: str
    DOBType: str
    LaborerDOB: LaborerDOB
    EducationId: str
    SpecialtyId: str
    WorkLocationId: str
    IBAN: str


class RequesterDetails(BaseModel):
    RequesterIdNo: str
    RequesterName: str
    RequesterUserId: str


class ContractDetails(BaseModel):
    OccupationId: str
    JobTitle: JobTitle
    LaborerJobNumber: str
    ContractTypeId: str
    ContractDurationId: str
    ContractPeriod: str
    ProbationPeriod: str
    WorkingHoursTypeId: str
    VacationPeriod: str
    Salary: str
    SalaryTypeId: str
    Allowances: dict
    StartDate: dict
    ExpiryDate: dict
    RenewalStatusId: str
    NoticePeriod: str
    AddedClauses: dict
    SalaryFrequency: str
    AdditionalAllowancesList: dict
    HoursPerWeek: str
    DaysPerWeek: str
    HoursPerDay: str
    OptionalArticles: dict


class Allowances(BaseModel):
    AllowancesItems: list[AllowanceItem]


class StartDate(BaseModel):
    HijriDate: str
    GregDate: str


class ExpiryDate(BaseModel):
    HijriDate: str
    GregDate: str


class AddedClauses(BaseModel):
    AddedClausesItems: list[AddedClauseItem]


class AdditionalAllowancesList(BaseModel):
    Item: list[AdditionalAllowanceItem]


class OptionalArticles(BaseModel):
    Period: str
    Location: str
    WorkField: str


class Body(BaseModel):
    EstablishmentDetails: EstablishmentDetails
    LaborerDetails: dict
    RequesterDetails: dict
    ContractDetails: dict
    LanguageId: str
    DateTypeId: str
    RelatedToId: int


class CreateNewContractRq(BaseModel):
    Header: Header
    Body: Body


class CreateNewContractRqPayload(BaseModel):
    CreateNewContractRq: CreateNewContractRq
