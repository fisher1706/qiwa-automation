from dataclasses import dataclass

# Temporary due to dataset dependency, will be removed  after UI part migration


@dataclass
class LoginPageLocators:
    LOGIN_FIELD = "#userId"
    PASSWORD_FIELD = "#password"
    CONTINUE_BUTTON = '//button[@type="submit"]'
    TWO_FA_FIELD = "#test-0"
    TWO_FA_FIELD_2 = "#test-1"
    TWO_FA_FIELD_3 = "#test-2"
    TWO_FA_FIELD_4 = "#test-3"
    SIGN_IN_BUTTON = "#submit"
    LOGOUT = "//*[contains(text(),'Logout')]"
    LOGOUT_WORKSPACE = "//*[contains(text(),'Log out')]"
    USER_INFO = '//div[@class="q-header__block q-user"]'
    USER_INFO_WORKSPACE = '//div[@data-testid="menu-trigger"]'
    LOCALIZATION_MENU = '//div[@data-component="MenuTrigger"]'
    EN_LOCAL = '//button[text()="English"]'


@dataclass
class WorkSpacesLocators:
    LMI_ADMIN_WORKSPACE = '(//button[@data-component="Tile"])[2]'


@dataclass
class BasePageLocators:
    BACK_HYPERLINK = '//*[@class="back-link"]'
    WEQ_TAB = '//*[@class="icon-services"]'
    DASHBOARD_TAB = '//*[@class="icon-dashboard"]'
    VIEW_DIMENSION_HYPERLINK = '//*[@href="/dimensions"]'
    SURVEY_QPRO_DETAILS_BUTTON = (
        '//*[contains(text(), "Auto test Question Pro")]/..//following-sibling::td[4]//button'
    )
    SURVEY_SS_DETAILS_BUTTON = (
        '//*[contains(text(), "Auto test Survey Sparrow ")]/..//following-sibling::td[4]//button'
    )
    SURVEY_IDS_ALL = '//td[@data-label="Id"]//*[text()]'
    DETAILS_BUTTON = '//td[@data-label="Id"]//*[text()]/../..//td[@data-label="Actions"]'
    SYNC_DROPDOWN = '//*[@data-testid="label"][ text()=" Sync survey "]'
    SYNC_SURVEY_OPTION = '(//*[@data-testid="item"][ text()=" {0} "])[2]'
    SPINNER_SYNC = '//*[@class="fas fa-sync-alt fa-spin"]'
    SURVEYS_NAMES_ALL = '//td[@data-label="Name"]//span[@class="column-wraper"][text()]'
    SURVEYS_NAMES_FAVORITE = '(//table[@class="table"])[1]//td[@data-label="Name"]//*[text()]'
    EMPTY_COLUMN = '//*[@class="is-empty"]'

    MESSAGE = '//div[@role="alert"]//div[@class="text"]'
    DELETE_BUTTON_MODAL = '//*[@data-testid][contains (text(),"Delete")]'
    CANCEL_BUTTON_MODAL = '//*[contains (text(),"Cancel")]'
    EDIT_BUTTON = '//*[contains(text(), "{0}")]/..//following-sibling::div/button[1]'
    CONFIRMATION_MODAL = '//div[@class="animation-content modal-content"]'
    DIMENSION_TITLE = '//*[@class="q-page-box__title"]'
    SPINNER = '//div[@class="row"]//span[@class="q-spinner-inner"]'
    CLOSE_CONFIRMATION_MODAL = '//button[@class="modal-close is-large"]'
    DIMENSION_TABS = '//span[contains(text(), "{0}")]'
    QUESTION_TAB = '//span[contains(text(), "Question")]'
    QUESTION_OPTIONS = '//h3[@class="tab-title d-flex align-items-center"]'
    SAVE_BUTTON = '//*[@data-testid="save"]'
    SUBMIT_BUTTON = '//button[@type="submit"]'
    NAME_FIELD_MODAL = '//input[@type="text"]'
    LOGIN_SUCCESS = '//p[@class="w-text--big"]'


@dataclass
class DimensionWeqLocators:
    CREATE_DIMENSION = '//*[contains (text(),"Create new dimension")]'
    DELETE_DIMENSION = '//*[contains(text(), "{0}")]/..//following-sibling::div/button[2]'
    NAME_AR = '//*[@data-testid="name"][@placeholder="أدخل اسم البعد"]'
    NAME_EN = '//*[@data-testid="name"][@placeholder="Enter dimension name"][@class="input"]'


@dataclass
class SurveyQuestionLocators:
    QUESTION_WEIGHT_FIELD = '//input[@data-testid="input"]'
    QUESTION_CODE = '//*[@class="code"]'
    MAX_ANSWER_SCORE = '//*[@class="code has-tooltip"]'
    ANSWER_WEIGHT_FIELD = '//input[@data-testid="input"][@data-child-weight]'
    QUESTION = (
        '//*[@class="tab-wrap has-children d-flex justify-content-between align-items-center"]'
    )
    QUESTION_TITLE = '//span[@class="holder"]'
    RESET_WEIGHTS_BUTTON = '//button[@data-testid="reset"]'
    CONFIRM_BUTTON = '//button[@data-testid="confirm"]'
    BLUR_STATE = '//*[@class="blur"]'


@dataclass
class DimensionDetailsLocators:
    ADD_QUESTION_BUTTON = '//button[@data-testid="add"]'
    ADD_QUESTION_MODAL_BUTTON = '//button[@class="q-btn q-btn--small"][contains (text(), "Add")]'
    QUESTIONS_NAME_COLUMN = '//div[@data-testid="question-name"]'
    QUESTIONS_NAME_DIMENSION = '//p[@data-testid="dimension-name"][@class="mr-5 mb-1 mt-1"]'
    REMOVE_QUESTION_BUTTON = '//button[@class="q-btn q-btn--small"]'


@dataclass
class RetailSectorWeqLocators:
    RECALCULATE_RESULT_BUTTON = '//button[@data-testid="recalculate"]'
    PUBLISH_RESULT_BUTTON = '//button[@data-testid="redirect"][text()=" Publish results "]'
    OVERALL_INDEX = '(//*[@data-testid="overall"]//span[@class="q-circle-chart__text-holder"])[1]'


@dataclass
class ResultDetailsLocators:
    RESULT_BUTTON = '//button[@data-testid="result"]'
    SPINNER_RESULT_DOWNLOAD = '//i[@class="fas fa-sync-alt fa-spin"]'
    CREATE_NEW_LINK_BUTTON = (
        '//button[@class="q-btn btn-sync-s ml-3 mr-3"][contains (text(), "Create new link")]'
    )
    LINK_NAMES_COLUMN = '//td[@data-label="Name"]//span[@style]'
    LINK_EDIT_BUTTON = '//button[contains (text(), "Edit")]'
    DELETE_BUTTON = '//button[contains (text(), "Delete")]'
    SURVEY_LINK = '//span[@class="link-holder has-tooltip"]'
    VIEWS_COLUMN = '//td[@data-label="Views"]//span[@style]'
    SPINNER_LANDING = '//div[@class="loading-icon"]'


@dataclass
class LandingLocators:
    BLOCK_ON_LANDING = '//div[@class="card"]//h3[@class="card--headline"][text()="{0}"]'
    RETAIL_SECTOR_BLOCK = (
        '//h5[@class="report-card--headline"][contains (text(),"The Retail Sector")]'
    )
    VIEW_FULL_REPORT_BUTTON = '//button[@class="report-button"]'
    COMPANY_LIST = (
        '//div[@class="environment-result"]//*[text()="All Retail Establishments results"]'
    )
    TOP_COMPANIES_BLOCK = '//div[@class="overall-main"]//div[@selecteddimension="totalIndex"]'
    COMPANY = '//*[@class="company-link"]'
    ENVIRONMENT_RANKING = '//div[@class="environment-ranking"]'
    INDEXES_VALUES = '//span[@class="ep-legend--value__counter"]//span'


@dataclass
class DashboardSurveyLocators:
    FAVORITE_SURVEY_CHECKBOX = "#favorite"
    TARGET_GROUP_DROPDOWN = "#pet-select"
    TARGET_GROUP_OPTION = '//option[@value="{0}"]'

    SURVEYS_INDIVIDUAL_CHECKBOX = '//label[@class="b-checkbox checkbox"]'
    SURVEY_INDIVIDUAL_CHECKBOX = '//*[contains(text(), "{0}")]/..//following-sibling::td[1]//label'
