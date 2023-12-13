import dataclasses

from data.data_portal.constants import (
    AboutUs,
    Admin,
    AllSectors,
    ContactUs,
    EmployeesChart,
    EstablishmentsChart,
    Footer,
    Header,
    HomePageHero,
    InsightBlock,
    Reports,
    Sector,
    SolutionBlock,
    SubscribeBlock,
    TrendingStatsBlock,
    TrustBlock,
    Variables,
    WorkforceChart,
)
from src.api.dataportal.schemas.response_mapping import WorkForceStatistics
from src.ui.pages.data_portal_pages.about_us_page import AboutUsPage
from src.ui.pages.data_portal_pages.all_sectors_page import AllSectorsPage
from src.ui.pages.data_portal_pages.contact_us_page import ContactUsPage
from src.ui.pages.data_portal_pages.footer_block import FooterBlock
from src.ui.pages.data_portal_pages.header_block import HeaderBlock
from src.ui.pages.data_portal_pages.home_page import (
    HomePage,
    InsightBlockLocators,
    SolutionBlockLocators,
    SubscribeBlockLocators,
    TrendingStatsBlockLocators,
    TrustBlockLocators,
)
from src.ui.pages.data_portal_pages.market_overview_page import (
    EmployeesChartLocators,
    EstablishmentsChartLocators,
    MarketOverViewPage,
    WorkforceBySectorLocators,
)
from src.ui.pages.data_portal_pages.privacy_policy_page import PrivacyPolicyPage
from src.ui.pages.data_portal_pages.report_page import ReportsPage
from src.ui.pages.data_portal_pages.sector_page import SectorPage


@dataclasses.dataclass
class FooterData:
    en_element_data = (
        (FooterBlock.SECTORS_TITLE, Footer.SECTORS_TITLE_EN),
        (FooterBlock.COMPANY_TITLE, Footer.COMPANY_TITLE_EN),
        (FooterBlock.ABOUT_US, Footer.ABOUT_US_EN),
        (FooterBlock.CONTACT_US, Footer.CONTACT_US_EN),
        (FooterBlock.VIEW_ALL_SECTORS, Footer.VIEW_ALL_SECTORS_EN),
        (FooterBlock.MARKET_OVERVIEW, Footer.MARKET_OVERVIEW_EN),
        (FooterBlock.TERMS_OF_USER, Footer.TERMS_OF_USER_EN),
        (FooterBlock.PRIVACY_POLICY, Footer.PRIVACY_POLICY_EN),
    )

    ar_element_data = (
        (FooterBlock.SECTORS_TITLE, Footer.SECTORS_TITLE_AR),
        (FooterBlock.COMPANY_TITLE, Footer.COMPANY_TITLE_AR),
        (FooterBlock.ABOUT_US, Footer.ABOUT_US_AR),
        (FooterBlock.CONTACT_US, Footer.CONTACT_US_AR),
        (FooterBlock.VIEW_ALL_SECTORS, Footer.VIEW_ALL_SECTORS_AR),
        (FooterBlock.MARKET_OVERVIEW, Footer.MARKET_OVERVIEW_AR),
        (FooterBlock.TERMS_OF_USER, Footer.TERMS_OF_USER_AR),
        (FooterBlock.PRIVACY_POLICY, Footer.PRIVACY_POLICY_AR),
    )


@dataclasses.dataclass
class HeaderData:
    en_element_data = (
        (HeaderBlock.SECTORS, Header.SECTORS_TITLE_EN),
        (HeaderBlock.MARKET_OVERVIEW, Header.MARKET_OVERVIEW_EN),
    )

    ar_element_data = (
        (HeaderBlock.SECTORS, Header.SECTORS_TITLE_AR),
        (HeaderBlock.MARKET_OVERVIEW, Header.MARKET_OVERVIEW_AR),
    )

    en_services_data = (
        (HeaderBlock.VIEW_ALL_SECTORS, Header.VIEW_ALL_SECTORS_EN),
        (HeaderBlock.ISIC_4_CLASSIFICATION, Header.ISIC_4_CLASSIFICATION_EN),
        (HeaderBlock.NITAQAT_CLASSIFICATION, Header.NITAQAT_CLASSIFICATION_EN),
    )

    ar_services_data = (
        (HeaderBlock.VIEW_ALL_SECTORS, Header.VIEW_ALL_SECTORS_AR),
        (HeaderBlock.ISIC_4_CLASSIFICATION, Header.ISIC_4_CLASSIFICATION_AR),
        (HeaderBlock.NITAQAT_CLASSIFICATION, Header.NITAQAT_CLASSIFICATION_AR),
    )


@dataclasses.dataclass
class HomePageDataSet:
    en_elements_data = (
        (HomePage.HERO_TITLE, HomePageHero.HERO_TITLE_EN),
        (TrendingStatsBlockLocators.DESCRIPTION, TrendingStatsBlock.DESCRIPTION_EN),
        (AllSectorsPage.SECTORS_CARD, AllSectors.SECTORS_NAME_EN),
        (
            InsightBlockLocators.SLIDER_LIST_DESCRIPTIONS,
            InsightBlock.SLIDER_LIST_DESCRIPTIONS_EN,
            InsightBlockLocators.FORWARD_BUTTON_NAV,
        ),
        (SolutionBlockLocators.ITEM_TITLE, SolutionBlock.ITEMS_EN),
        (SolutionBlockLocators.ITEM_DESCRIPTION, SolutionBlock.ITEMS_DESCRIPTION_EN),
        (TrustBlockLocators.PROVIDED, TrustBlock.PROVIDED_TITLE_EN),
        (TrustBlockLocators.INFO_DATA, TrustBlock.TRUST_INFO_EN),
    )

    ar_elements_data = (
        (HomePage.HERO_TITLE, HomePageHero.HERO_TITLE_AR),
        (TrendingStatsBlockLocators.DESCRIPTION, TrendingStatsBlock.DESCRIPTION_AR),
        (AllSectorsPage.SECTORS_CARD, AllSectors.SECTORS_NAME_AR),
        (
            InsightBlockLocators.SLIDER_LIST_DESCRIPTIONS,
            InsightBlock.SLIDER_LIST_DESCRIPTIONS_AR,
            InsightBlockLocators.FORWARD_BUTTON_NAV,
        ),
        (SolutionBlockLocators.ITEM_TITLE, SolutionBlock.ITEMS_AR),
        (SolutionBlockLocators.ITEM_DESCRIPTION, SolutionBlock.ITEMS_DESCRIPTION_AR),
        (TrustBlockLocators.PROVIDED, TrustBlock.PROVIDED_TITLE_AR),
        (TrustBlockLocators.INFO_DATA, TrustBlock.TRUST_INFO_AR),
    )

    en_element_data = (
        (HomePage.HERO_DESCRIPTION, HomePageHero.HERO_DESCRIPTION_EN),
        (HomePage.MARKET_OVERVIEW, Footer.MARKET_OVERVIEW_EN),
        (HomePage.BLOCK_DATA_HERO_1, HomePageHero.BLOCK_DATA_HERO_1_EN),
        (HomePage.BLOCK_DATA_HERO_2, HomePageHero.BLOCK_DATA_HERO_2_EN),
        (HomePage.BLOCK_DATA_HERO_3, HomePageHero.BLOCK_DATA_HERO_3_EN),
        (TrendingStatsBlockLocators.TITLE, TrendingStatsBlock.TITLE_EN),
        (
            TrendingStatsBlockLocators.EXPLORE_STATS_TITLE,
            TrendingStatsBlock.EXPLORE_STATS_TITLE_EN,
        ),
        (TrendingStatsBlockLocators.EXPLORE_CARD_TITLE, TrendingStatsBlock.EXPLORE_CARD_TITLE_EN),
        (SectorPage.CHART_TITLE, Sector.TITLE_EN),
        (SectorPage.CHART_DESCRIPTION, Sector.DESCRIPTION_EN),
        (SectorPage.CHART_TITLE_HEADER, Sector.TITLE_HEADER_EN),
        (SectorPage.CHART_EXPLORE_BUTTON, Sector.EXPLORE_BUTTON_EN),
        (AllSectorsPage.TITLE, AllSectors.TITLE_EN),
        (AllSectorsPage.VIEW_ALL_SECTORS_BUTTON, Footer.VIEW_ALL_SECTORS_EN),
        (InsightBlockLocators.TITLE, InsightBlock.TITLE_EN),
        (InsightBlockLocators.DESCRIPTION, InsightBlock.DESCRIPTION_EN),
        (InsightBlockLocators.EXPLORE_BUTTON, HomePageHero.EXPLORE_BUTTON_EN),
        (SolutionBlockLocators.TITLE, SolutionBlock.TITLE_EN),
        (SolutionBlockLocators.DESCRIPTION, SolutionBlock.DESCRIPTION_EN),
        (TrustBlockLocators.TITLE, TrustBlock.TITLE_EN),
        (TrustBlockLocators.DESCRIPTION, TrustBlock.DESCRIPTION_EN),
        (ContactUsPage.TITLE_BLOCK, ContactUs.BLOCK_TITLE_EN),
        (ContactUsPage.DESCRIPTION_BLOCK, ContactUs.DESCRIPTION_EN),
        (ContactUsPage.BUTTON, ContactUs.BUTTON_EN),
        (SubscribeBlockLocators.TITLE, SubscribeBlock.TITLE_EN),
        (SubscribeBlockLocators.DESCRIPTION, SubscribeBlock.DESCRIPTION_EN),
        (SubscribeBlockLocators.BUTTON, SubscribeBlock.BUTTON_EN),
    )

    ar_element_data = (
        (HomePage.HERO_DESCRIPTION, HomePageHero.HERO_DESCRIPTION_AR),
        (HomePage.MARKET_OVERVIEW, Footer.MARKET_OVERVIEW_AR),
        (HomePage.BLOCK_DATA_HERO_1, HomePageHero.BLOCK_DATA_HERO_1_AR),
        (HomePage.BLOCK_DATA_HERO_2, HomePageHero.BLOCK_DATA_HERO_2_AR),
        (HomePage.BLOCK_DATA_HERO_3, HomePageHero.BLOCK_DATA_HERO_3_AR),
        (TrendingStatsBlockLocators.TITLE, TrendingStatsBlock.TITLE_AR),
        (
            TrendingStatsBlockLocators.EXPLORE_STATS_TITLE,
            TrendingStatsBlock.EXPLORE_STATS_TITLE_AR,
        ),
        (TrendingStatsBlockLocators.EXPLORE_CARD_TITLE, TrendingStatsBlock.EXPLORE_CARD_TITLE_AR),
        (SectorPage.CHART_TITLE, Sector.TITLE_AR),
        (SectorPage.CHART_DESCRIPTION, Sector.DESCRIPTION_AR),
        (SectorPage.CHART_TITLE_HEADER, Sector.TITLE_HEADER_AR),
        (SectorPage.CHART_EXPLORE_BUTTON, Sector.EXPLORE_BUTTON_AR),
        (AllSectorsPage.TITLE, AllSectors.TITLE_AR),
        (AllSectorsPage.VIEW_ALL_SECTORS_BUTTON, Footer.VIEW_ALL_SECTORS_AR),
        (InsightBlockLocators.TITLE, InsightBlock.TITLE_AR),
        (InsightBlockLocators.DESCRIPTION, InsightBlock.DESCRIPTION_AR),
        (InsightBlockLocators.EXPLORE_BUTTON, HomePageHero.EXPLORE_BUTTON_AR),
        (SolutionBlockLocators.TITLE, SolutionBlock.TITLE_AR),
        (SolutionBlockLocators.DESCRIPTION, SolutionBlock.DESCRIPTION_AR),
        (TrustBlockLocators.TITLE, TrustBlock.TITLE_AR),
        (TrustBlockLocators.DESCRIPTION, TrustBlock.DESCRIPTION_AR),
        (ContactUsPage.TITLE_BLOCK, ContactUs.BLOCK_TITLE_AR),
        (ContactUsPage.DESCRIPTION_BLOCK, ContactUs.DESCRIPTION_AR),
        (ContactUsPage.BUTTON, ContactUs.BUTTON_AR),
        (SubscribeBlockLocators.TITLE, SubscribeBlock.TITLE_AR),
        (SubscribeBlockLocators.DESCRIPTION, SubscribeBlock.DESCRIPTION_AR),
        (SubscribeBlockLocators.BUTTON, SubscribeBlock.BUTTON_AR),
    )

    chart_dropdown_option = (
        (
            SectorPage.CHART_TYPE_SECTION,
            SectorPage.CHART_DROPDOWN,
            SectorPage.CHART_DROPDOWN_OPTIONS,
            EmployeesChart.DOUGHNUT_CHART,
            False,
        ),
        (
            SectorPage.CHART_CALENDAR_SECTION,
            SectorPage.CHART_DROPDOWN,
            SectorPage.CHART_DROPDOWN_OPTIONS,
            EmployeesChart.CALENDAR_OPTIONS,
            True,
        ),
    )


@dataclasses.dataclass
class MarketOverviewData:
    employee_establish_data = (
        (
            MarketOverViewPage.EMPLOYEE,
            1,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.NOOFEMPLOYEES,
            None,
        ),
        (
            MarketOverViewPage.ESTABLISHMENTS,
            10,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.NUMBEROFESTABLISHMENTS,
            None,
        ),
        (
            EmployeesChartLocators.TOTAL,
            1,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.NOOFEMPLOYEES,
            None,
        ),
        (
            EmployeesChartLocators.TOTAL_MALE,
            7,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.TOTAL_MALE,
            EmployeesChart.GO_TO_GENDER_TAB,
        ),
        (
            EmployeesChartLocators.TOTAL_FEMALE,
            7,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.TOTAL_FEMALE,
            EmployeesChart.GO_TO_GENDER_TAB,
        ),
        (
            EstablishmentsChartLocators.TOTAL,
            10,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.NUMBEROFESTABLISHMENTS,
            None,
        ),
        (
            EstablishmentsChartLocators.TOTAL,
            20,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.NOOFUNIFIEDCOMPANIES,
            EstablishmentsChart.PICK_UNIFIED_OPTION,
        ),
        (
            EstablishmentsChartLocators.TOTAL,
            25,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.NUMBEROFENTITIES,
            EstablishmentsChart.PICK_ENTITIES_OPTION,
        ),
    )

    workforce_by_sector_data = (
        (
            WorkforceBySectorLocators.TOTAL,
            18,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.NOOFEMPLOYEE,
            None,
        ),
        (
            WorkforceBySectorLocators.TOTAL_ALL_SECTORS_TAB,
            59,
            [{"name": "StartDate", "gt": {}}, {"name": "EndDate", "lt": {}}],
            WorkForceStatistics.NOOFEMPLOYEE,
            WorkforceChart.ALL_SECTORS,
        ),
    )


@dataclasses.dataclass
class ContactUsDataSet:
    setup_data = (
        (Variables.AUTOTEST, Variables.EMAIL, Variables.generate_string(30), Variables.COMPANY),
        (Variables.AUTOTEST, Variables.EMAIL, Variables.generate_string(2500), Variables.COMPANY),
        (Variables.AUTOTEST, Variables.EMAIL, Variables.generate_string(30), None),
        (Variables.AUTOTEST, Variables.EMAIL, Variables.generate_string(2500), None),
    )

    negative_data = (
        (Variables.EMPTY, Variables.EMPTY, Variables.EMPTY),
        (Variables.EMPTY, Variables.EMAIL, Variables.generate_string(30)),
        (Variables.AUTOTEST, "", Variables.generate_string(30)),
        (Variables.AUTOTEST, Variables.EMAIL_WITHOUT_AT, Variables.generate_string(30)),
        (Variables.AUTOTEST, Variables.EMAIL_WITHOUT_DOT, Variables.generate_string(30)),
        (Variables.AUTOTEST, Variables.EMAIL_WITHOUT_PREFIX, Variables.generate_string(30)),
        (Variables.AUTOTEST, Variables.EMAIL_WITHOUT_DOMAIN, Variables.generate_string(30)),
        (Variables.AUTOTEST, Variables.EMAIL, Variables.EMPTY),
        (Variables.AUTOTEST, Variables.EMAIL, Variables.generate_string(29)),
        (Variables.AUTOTEST, Variables.EMAIL, Variables.generate_string(2501)),
    )

    en_element_data = (
        (ContactUsPage.TITLE, ContactUs.TITLE_EN, False),
        (ContactUsPage.SEND_BUTTON, ContactUs.SEND_BUTTON_EN, False),
        (ContactUsPage.BACK_TO_HOME, ContactUs.BACK_BUTTON_EN, True),
        (ContactUsPage.TITLE_SUCCESS, ContactUs.TITLE_SUCCESS_EN, True),
        (ContactUsPage.DESCR_SUCCESS, ContactUs.DESCR_SUCCESS_EN, True),
    )

    ar_element_data = (
        (ContactUsPage.TITLE, ContactUs.TITLE_AR, False),
        (ContactUsPage.SEND_BUTTON, ContactUs.SEND_BUTTON_AR, False),
        (ContactUsPage.BACK_TO_HOME, ContactUs.BACK_BUTTON_AR, True),
        (ContactUsPage.TITLE_SUCCESS, ContactUs.TITLE_SUCCESS_AR, True),
        (ContactUsPage.DESCR_SUCCESS, ContactUs.DESCR_SUCCESS_AR, True),
    )


@dataclasses.dataclass
class AboutUsData:
    en_element_data = (
        (AboutUsPage.HERO_TITLE, AboutUs.HERO_TITLE_EN),
        (AboutUsPage.HERO_DESCRIPTION, AboutUs.HERO_DESCRIPTION_EN),
        (AboutUsPage.MISSION_TITLE, AboutUs.MISSION_TITLE_EN),
        (AboutUsPage.BENEFITS_TITLE, AboutUs.BENEFITS_TITLE_EN),
        (AboutUsPage.BELIEVE_TITLE, AboutUs.BELIEVE_TITLE_EN),
        (AboutUsPage.QIWA_SA_TITLE, AboutUs.QIWA_SA_TITLE_AR),
        (AboutUsPage.QIWA_VISIT_TITLE, AboutUs.QIWA_VISIT_TITLE_EN),
    )

    ar_element_data = (
        (AboutUsPage.HERO_TITLE, AboutUs.HERO_TITLE_AR),
        (AboutUsPage.HERO_DESCRIPTION, AboutUs.HERO_DESCRIPTION_AR),
        (AboutUsPage.MISSION_TITLE, AboutUs.MISSION_TITLE_AR),
        (AboutUsPage.BENEFITS_TITLE, AboutUs.BENEFITS_TITLE_AR),
        (AboutUsPage.BELIEVE_TITLE, AboutUs.BELIEVE_TITLE_AR),
        (AboutUsPage.QIWA_SA_TITLE, AboutUs.QIWA_SA_TITLE_AR),
        (AboutUsPage.QIWA_VISIT_TITLE, AboutUs.QIWA_VISIT_TITLE_AR),
    )

    en_elements_data = (
        (AboutUsPage.MISSION_CARD_TITLE, AboutUs.MISSION_CARD_TITLE_EN),
        (AboutUsPage.MISSION_CARD_DESCRIPTION, AboutUs.MISSION_CARD_DESCRIPTION_EN),
        (AboutUsPage.BENEFITS_CARD_TITLE, AboutUs.BENEFITS_CARD_TITLE_EN),
        (AboutUsPage.BENEFITS_CARD_DESCRIPTION, AboutUs.BENEFITS_CARD_DESCRIPTION_EN),
        (AboutUsPage.BELIEVE_CARD_TITLE, AboutUs.BELIEVE_CARD_TITLE_EN),
        (AboutUsPage.BELIEVE_CARD_DESCRIPTION, AboutUs.BELIEVE_CARD_DESCRIPTION_EN),
        (AboutUsPage.QIWA_SA_DESCRIPTION, AboutUs.QIWA_SA_DESCRIPTION_EN),
        (AboutUsPage.QIWA_VISIT_LINK, AboutUs.QIWA_VISIT_LINK_EN),
    )

    ar_elements_data = (
        (AboutUsPage.MISSION_CARD_TITLE, AboutUs.MISSION_CARD_TITLE_AR),
        (AboutUsPage.MISSION_CARD_DESCRIPTION, AboutUs.MISSION_CARD_DESCRIPTION_AR),
        (AboutUsPage.BENEFITS_CARD_TITLE, AboutUs.BENEFITS_CARD_TITLE_AR),
        (AboutUsPage.BENEFITS_CARD_DESCRIPTION, AboutUs.BENEFITS_CARD_DESCRIPTION_AR),
        (AboutUsPage.BELIEVE_CARD_TITLE, AboutUs.BELIEVE_CARD_TITLE_AR),
        (AboutUsPage.BELIEVE_CARD_DESCRIPTION, AboutUs.BELIEVE_CARD_DESCRIPTION_AR),
        (AboutUsPage.QIWA_SA_DESCRIPTION, AboutUs.QIWA_SA_DESCRIPTION_AR),
        (AboutUsPage.QIWA_VISIT_LINK, AboutUs.QIWA_VISIT_LINK_AR),
    )


@dataclasses.dataclass
class AllSectorsData:
    en_element_data = (
        (AllSectorsPage.HERO_TITLE, AllSectors.HERO_TITLE_EN),
        (AllSectorsPage.ISIC_4_CLASSIFICATION, AllSectors.ISIC_4_CLASSIFICATION_EN),
        (AllSectorsPage.NITAQAT_CLASSIFICATION, AllSectors.NITAQAT_CLASSIFICATION_EN),
    )

    ar_element_data = (
        (AllSectorsPage.HERO_TITLE, AllSectors.HERO_TITLE_AR),
        (AllSectorsPage.ISIC_4_CLASSIFICATION, AllSectors.ISIC_4_CLASSIFICATION_AR),
        (AllSectorsPage.NITAQAT_CLASSIFICATION, AllSectors.NITAQAT_CLASSIFICATION_AR),
    )

    en_elements_data = (
        (
            AllSectorsPage.ISIC_4_CLASSIFICATION,
            AllSectorsPage.SECTOR_TITLE,
            AllSectors.ISIC_4_SECTORS_EN,
        ),
        (
            AllSectorsPage.NITAQAT_CLASSIFICATION,
            AllSectorsPage.SECTOR_TITLE,
            AllSectors.NITAQAT_SECTORS_EN,
        ),
    )

    ar_elements_data = (
        (
            AllSectorsPage.ISIC_4_CLASSIFICATION,
            AllSectorsPage.SECTOR_TITLE,
            AllSectors.ISIC_4_SECTORS_AR,
        ),
        (
            AllSectorsPage.NITAQAT_CLASSIFICATION,
            AllSectorsPage.SECTOR_TITLE,
            AllSectors.NITAQAT_SECTORS_AR,
        ),
    )

    en_search_data = (
        (AllSectors.SEARCHING_CRITERIA_EN, AllSectors.SEARCH_ITEMS_EN),
        (Variables.AUTOTEST, AllSectors.NO_RESULTS_EN),
    )
    ar_search_data = (
        (AllSectors.SEARCHING_CRITERIA_AR, AllSectors.SEARCH_ITEMS_AR),
        (Variables.AUTOTEST, AllSectors.NO_RESULTS_AR),
    )


@dataclasses.dataclass
class SectorData:
    nitaqat_sector_ids_data = [
        2,
        47,
        48,
        54,
        55,
        56,
        57,
        67,
        76,
        84,
        410,
        421,
        430,
        450,
        451,
        460,
        462,
        463,
        464,
        465,
        466,
        467,
        468,
        469,
        471,
        472,
        473,
        474,
        475,
        476,
        477,
        479,
        480,
        481,
        491,
        492,
        493,
        494,
        495,
        496,
        497,
        499,
    ]
    economic_sector_ids_data = [
        "I",
        "U",
        "T",
        "N",
        "A",
        "R",
        "F",
        "P",
        "D",
        "K",
        "Q",
        "J",
        "C",
        "B",
        "S",
        "M",
        "O",
        "L",
        "H",
        "E",
        "G",
    ]
    sector_data = (
        (
            SectorPage.EMPLOYEE_VALUES,
            17,
            [
                {"name": "StartDate", "gt": {}},
                {"name": "EndDate", "lt": {}},
                {"name": "EconomicActivityId", "eq": {}},
            ],
            WorkForceStatistics.TOTAL_EMPLOYEES,
            None,
        ),
        (
            SectorPage.ESTABLISH_VALUES,
            23,
            [
                {"name": "StartDate", "gt": {}},
                {"name": "EndDate", "lt": {}},
                {"name": "EconomicActivityId", "eq": {}},
            ],
            WorkForceStatistics.TOTAL_ESTABLISHMENTS,
            None,
        ),
        (
            EmployeesChartLocators.TOTAL,
            17,
            [
                {"name": "StartDate", "gt": {}},
                {"name": "EndDate", "lt": {}},
                {"name": "EconomicActivityId", "eq": {}},
            ],
            WorkForceStatistics.TOTAL_EMPLOYEES,
            None,
        ),
        (
            EmployeesChartLocators.TOTAL_MALE,
            17,
            [
                {"name": "StartDate", "gt": {}},
                {"name": "EndDate", "lt": {}},
                {"name": "EconomicActivityId", "eq": {}},
            ],
            WorkForceStatistics.TOTAL_MALE,
            EmployeesChart.GO_TO_GENDER_TAB,
        ),
        (
            EmployeesChartLocators.TOTAL_FEMALE,
            17,
            [
                {"name": "StartDate", "gt": {}},
                {"name": "EndDate", "lt": {}},
                {"name": "EconomicActivityId", "eq": {}},
            ],
            WorkForceStatistics.TOTAL_FEMALE,
            EmployeesChart.GO_TO_GENDER_TAB,
        ),
        (
            EstablishmentsChartLocators.TOTAL,
            23,
            [
                {"name": "StartDate", "gt": {}},
                {"name": "EndDate", "lt": {}},
                {"name": "EconomicActivityId", "eq": {}},
            ],
            WorkForceStatistics.TOTAL_ESTABLISHMENTS,
            None,
        ),
        (
            EstablishmentsChartLocators.TOTAL,
            21,
            [
                {"name": "StartDate", "gt": {}},
                {"name": "EndDate", "lt": {}},
                {"name": "EconomicActivityId", "eq": {}},
            ],
            WorkForceStatistics.TOTAL_UNIFIED_COMPANIES,
            EstablishmentsChart.PICK_UNIFIED_OPTION,
        ),
        (
            EstablishmentsChartLocators.TOTAL,
            22,
            [
                {"name": "StartDate", "gt": {}},
                {"name": "EndDate", "lt": {}},
                {"name": "EconomicActivityId", "eq": {}},
            ],
            WorkForceStatistics.TOTAL_ENTITIES,
            EstablishmentsChart.PICK_ENTITIES_OPTION,
        ),
    )


@dataclasses.dataclass
class ReportDataSet:
    en_elements_data = (
        (ReportsPage.TOPIC_TITLES, Reports.TOPIC_TITLES_EN),
        (ReportsPage.TOPIC_DESCRIPTIONS, Reports.TOPIC_DESCRIPTIONS_EN),
    )

    ar_elements_data = (
        (ReportsPage.TOPIC_TITLES, Reports.TOPIC_TITLES_AR),
        (ReportsPage.TOPIC_DESCRIPTIONS, Reports.TOPIC_DESCRIPTIONS_AR),
    )


@dataclasses.dataclass
class PrivacyPolicyData:
    privacy_element_ids = [
        "TITLE, xlsx row - 4",
        "GEN_INFO_TITLE, xlsx row - 5",
        "READ_PARAGRAPH_TITLE, xlsx row - 6",
        "READ_PARAGRAPH_TEXT, xlsx row - 7",
        "INFO_GIVE_PARAGRAPH_TITLE, xlsx row - 8",
        "INFO_GIVE_PARAGRAPH_TEXT, xlsx row - 9",
        "INFO_COLLECT_PARAGRAPH_TITLE, xlsx row - 10",
        "INFO_COLLECT_PARAGRAPH_TEXT, xlsx row - 11",
        "INFO_COLLECT_PARAGRAPH_LIST, xlsx row - 12",
        "INFO_RECEIVE_PARAGRAPH_TITLE, xlsx row - 13",
        "INFO_RECEIVE_PARAGRAPH_TEXT, xlsx row - 14",
        "DETAILS_TITLE, xlsx row - 15",
        "COOKIES_TITLE, xlsx row - 16",
        "COOKIES_PARAGRAPH_1, xlsx row - 17",
        "USE_COOKIES_TITLE, xlsx row - 18",
        "USE_COOKIES_LIST, xlsx row - 19",
        "COOKIES_PARAGRAPH_2, xlsx row - 20",
        "COOKIES_PARAGRAPH_3, xlsx row - 21",
        "USES_MADE_OF_INFO_TITLE, xlsx row - 22",
        "USES_MADE_OF_INFO_PARAGRAPH, xlsx row - 23",
        "USES_MADE_OF_INFO_LIST, xlsx row - 24",
        "INFO_RECEIVE_TITLE, xlsx row - 25",
        "INFO_RECEIVE_PARAGRAPH, xlsx row - 26",
        "DISCLOSURE_INFO_TITLE, xlsx row - 27",
        "DISCLOSURE_INFO_PARAGRAPH, xlsx row - 28",
        "DISCLOSURE_INFO_LIST, xlsx row - 29",
        "CONSENT_TITLE, xlsx row - 30",
        "CONSENT_PARAGRAPH_1, xlsx row - 31",
        "CONSENT_PARAGRAPH_2, xlsx row - 32",
        "CONSENT_PARAGRAPH_3, xlsx row - 33",
        "CONSENT_PARAGRAPH_4, xlsx row - 34",
        "YOUR_RIGHTS_TITLE, xlsx row - 35",
        "YOUR_RIGHTS_PARAGRAPH_1, xlsx row - 36",
        "YOUR_RIGHTS_PARAGRAPH_2, xlsx row - 37",
        "CHANGES_TITLE, xlsx row - 38",
        "CHANGES_PARAGRAPH_1, xlsx row - 39",
        "CHANGES_PARAGRAPH_2, xlsx row - 40",
    ]

    privacy_elements = (
        (PrivacyPolicyPage.TITLE, 4),
        (PrivacyPolicyPage.GEN_INFO_TITLE, 5),
        (PrivacyPolicyPage.READ_PARAGRAPH_TITLE, 6),
        (PrivacyPolicyPage.READ_PARAGRAPH_TEXT, 7),
        (PrivacyPolicyPage.INFO_GIVE_PARAGRAPH_TITLE, 8),
        (PrivacyPolicyPage.INFO_GIVE_PARAGRAPH_TEXT, 9),
        (PrivacyPolicyPage.INFO_COLLECT_PARAGRAPH_TITLE, 10),
        (PrivacyPolicyPage.INFO_COLLECT_PARAGRAPH_TEXT, 11),
        (PrivacyPolicyPage.INFO_COLLECT_PARAGRAPH_LIST, 12),
        (PrivacyPolicyPage.INFO_RECEIVE_PARAGRAPH_TITLE, 13),
        (PrivacyPolicyPage.INFO_RECEIVE_PARAGRAPH_TEXT, 14),
        (PrivacyPolicyPage.DETAILS_TITLE, 15),
        (PrivacyPolicyPage.COOKIES_TITLE, 16),
        (PrivacyPolicyPage.COOKIES_PARAGRAPH_1, 17),
        (PrivacyPolicyPage.USE_COOKIES_TITLE, 18),
        (PrivacyPolicyPage.USE_COOKIES_LIST, 19),
        (PrivacyPolicyPage.COOKIES_PARAGRAPH_2, 20),
        (PrivacyPolicyPage.COOKIES_PARAGRAPH_3, 21),
        (PrivacyPolicyPage.USES_MADE_OF_INFO_TITLE, 22),
        (PrivacyPolicyPage.USES_MADE_OF_INFO_PARAGRAPH, 23),
        (PrivacyPolicyPage.USES_MADE_OF_INFO_LIST, 24),
        (PrivacyPolicyPage.INFO_RECEIVE_TITLE, 25),
        (PrivacyPolicyPage.INFO_RECEIVE_PARAGRAPH, 26),
        (PrivacyPolicyPage.DISCLOSURE_INFO_TITLE, 27),
        (PrivacyPolicyPage.DISCLOSURE_INFO_PARAGRAPH, 28),
        (PrivacyPolicyPage.DISCLOSURE_INFO_LIST, 29),
        (PrivacyPolicyPage.CONSENT_TITLE, 30),
        (PrivacyPolicyPage.CONSENT_PARAGRAPH_1, 31),
        (PrivacyPolicyPage.CONSENT_PARAGRAPH_2, 32),
        (PrivacyPolicyPage.CONSENT_PARAGRAPH_3, 33),
        (PrivacyPolicyPage.CONSENT_PARAGRAPH_4, 34),
        (PrivacyPolicyPage.YOUR_RIGHTS_TITLE, 35),
        (PrivacyPolicyPage.YOUR_RIGHTS_PARAGRAPH_1, 36),
        (PrivacyPolicyPage.YOUR_RIGHTS_PARAGRAPH_2, 37),
        (PrivacyPolicyPage.CHANGES_TITLE, 38),
        (PrivacyPolicyPage.CHANGES_PARAGRAPH_1, 39),
        (PrivacyPolicyPage.CHANGES_PARAGRAPH_2, 40),
    )


@dataclasses.dataclass
class AdminData:
    invalid_data = (
        (Admin.INVALID_LOGIN, Admin.PASSWORD),
        (Admin.LOGIN, Admin.INVALID_PASSWORD),
        (Admin.INVALID_LOGIN, Admin.INVALID_PASSWORD),
    )

    invalid_duration = (0, -1, 0.9)

    file_format = (Admin.PNG, Admin.GIF, Admin.JPG, Admin.JPEG, Admin.WEBP)
    other_file_format = (Admin.DOC, Admin.ICO, Admin.TXT, Admin.PDF)
    file_format_less_1280 = (
        Admin.PNG_640,
        Admin.GIF_640,
        Admin.JPG_640,
        Admin.JPEG_640,
        Admin.WEBP_640,
    )

    criteria = (
        (Admin.AUTOMATION, None, None, None),
        (Admin.AUTOMATION, Admin.PUBLISHED, None, None),
        (Admin.AUTOMATION, None, Admin.ENGLISH_FILTER, None),
        (Admin.AUTOMATION, None, None, Admin.AUTOMATION),
        (Admin.AUTOMATION, Admin.PUBLISHED, Admin.ENGLISH_FILTER, None),
        (Admin.AUTOMATION, Admin.PUBLISHED, Admin.ARABIC_FILTER, None),
        (Admin.AUTOMATION, Admin.PUBLISHED, None, Admin.AUTOMATION),
        (Admin.AUTOMATION, None, Admin.ENGLISH_FILTER, Admin.AUTOMATION),
        (None, Admin.PUBLISHED, None, None),
        (None, Admin.PUBLISHED, Admin.ENGLISH_FILTER, None),
        (None, Admin.PUBLISHED, Admin.ARABIC_FILTER, None),
        (None, Admin.PUBLISHED, None, Admin.AUTOMATION),
        (None, Admin.PUBLISHED, Admin.ENGLISH_FILTER, Admin.AUTOMATION),
        (None, Admin.PUBLISHED, Admin.ARABIC_FILTER, Admin.AUTOMATION),
        (None, None, Admin.ENGLISH_FILTER, None),
        (None, None, Admin.ENGLISH_FILTER, Admin.AUTOMATION),
        (None, None, None, Admin.AUTOMATION),
    )

    format_text = (
        Admin.BOLD,
        Admin.ITALIC,
        Admin.UNDERLINE,
        Admin.STRIKETHROUGH,
        Admin.SUBSCRIPT,
        Admin.SUPERSCRIPT,
    )

    alignment_text = (Admin.ALIGN_LEFT, Admin.ALIGN_CENTER, Admin.ALIGN_RIGHT, Admin.ALIGN_JUSTIFY)

    card_size = (
        Admin.PERCENTAGE_33,
        Admin.PERCENTAGE_66,
        Admin.PERCENTAGE_100,
        Admin.PERCENTAGE_MIX,
    )
