import dataclasses
import random

TRANSLATION_XLSX = "Translations Qiwa Data.xlsx"


@dataclasses.dataclass
class Links:
    REPORT = "https://data.qiwa.info/report/{index}"
    REPORTS = "https://data.qiwa.info/reports"
    TWITTER = "https://twitter.com/qiwa_sa"
    LINKEDIN = "https://sa.linkedin.com/showcase/qiwa-sa/"
    YOUTUBE = "https://www.youtube.com/qiwa_sa"
    QIWA_SA = "https://qiwa.sa/"
    TAKAMOL = "https://takamolholding.com/en/"
    HUMAN_RESOURCES = "https://www.hrsd.gov.sa/"

    HOME_PAGE = "https://data.qiwa.info/"
    VIEW_ALL_SECTORS = "https://data.qiwa.info/sectors"
    MARKET_OVERVIEW = "https://data.qiwa.info/market-overview"
    TERMS_OF_USER = "https://qiwa.sa/en/terms-and-conditions"
    PRIVACY_POLICY = "https://data.qiwa.info/privacy-policy"
    ABOUT_US = "https://data.qiwa.info/about-us"
    CONTACT_US = "https://data.qiwa.info/contact-us"
    WORKFORCE_STATISTICS = "https://data.qiwa.info/market-overview#workforce-statistics"
    ESTABLISHMENT_STATISTICS = "https://data.qiwa.info/market-overview#establishments"
    FINANCE_SECTOR = "https://data.qiwa.info/sector/?id=480&type=NITAQAT&colorIndex=0"
    OPERATIONS_SECTOR = "https://data.qiwa.info/sector/451?type=NITAQAT&colorIndex=0"
    MANUFACTURING_SECTOR = "https://data.qiwa.info/sector/430?type=NITAQAT&colorIndex=1"
    LAND_TRANSPORT_SECTOR = "https://data.qiwa.info/sector/471?type=NITAQAT&colorIndex=2"
    SOCIAL_SERVICE_SECTOR = "https://data.qiwa.info/sector/491?type=NITAQAT&colorIndex=3"
    CONSTRUCTION_SECTOR = "https://data.qiwa.info/sector/450?type=NITAQAT&colorIndex=4"


@dataclasses.dataclass
class Footer:
    SECTORS_TITLE_EN = "Sectors"
    SECTORS_TITLE_AR = "نشاط اقتصادي"

    COMPANY_TITLE_EN = "Company"
    COMPANY_TITLE_AR = "المنشأة"

    VIEW_ALL_SECTORS_EN = "View all sectors"
    VIEW_ALL_SECTORS_AR = "عرض جميع الأنشطة"
    MARKET_OVERVIEW_EN = "Market overview"
    MARKET_OVERVIEW_AR = "نظرة عامة على سوق العمل"

    TERMS_OF_USER_EN = "Terms of use"
    TERMS_OF_USER_AR = "تعليمات الاستخدام"
    PRIVACY_POLICY_EN = "Privacy policy"
    PRIVACY_POLICY_AR = "سياسات الخصوصية"

    ABOUT_US_EN = "About us"
    ABOUT_US_AR = "من نحن"
    CONTACT_US_EN = "Contact us"
    CONTACT_US_AR = "تواصل معنا"

    SECTORS_ITEM_EN = None
    SECTORS_ITEM_AR = None


@dataclasses.dataclass
class Header:
    VIEW_ALL_SECTORS_EN = "View all sectors"
    VIEW_ALL_SECTORS_AR = "عرض جميع الأنشطة"
    MARKET_OVERVIEW_EN = "Market overview"
    MARKET_OVERVIEW_AR = "نظرة عامة على سوق العمل"

    SECTORS_TITLE_EN = "Sectors"
    SECTORS_TITLE_AR = "نشاط اقتصادي"

    ECONOMIC_ACTIVITIES_EN = "Economic Activities"
    ECONOMIC_ACTIVITIES_AR = "الأنشطة الاقتصادية"
    NITAQAT_ACTIVITIES_EN = "Nitaqat Activities"
    NITAQAT_ACTIVITIES_AR = "الأنشطة حسب تصنيف نطاقات"

    SECTORS_ITEM_EN = None
    SECTORS_ITEM_AR = None


@dataclasses.dataclass
class HomePageHero:
    HERO_TITLE_EN = ["Get insights\non Saudi Arabia\nlabor market"]
    HERO_TITLE_AR = ["اطلع على\nإحصائيات سوق\nالعمل السعودي"]
    HERO_DESCRIPTION_EN = (
        "Get access to key statistics and indicators for different sectors. Explore employee and "
        "establishment statistics, analyze sector metrics, and view retrospective data."
    )
    HERO_DESCRIPTION_AR = (
        "إحصائيات ومؤشرات لمختلف القطاعات "
        "في سوق العمل السعودي. تصفح إحصائيات الموظفين والمنشآت وقارن بين القطاعات"
    )
    MARKET_OVERVIEW_HERO_AR = "نظرة عامة على سوق العمل"

    BLOCK_DATA_HERO_1_EN = "Growth of labor market for last 5 years"
    BLOCK_DATA_HERO_1_AR = "النمو في سوق العمل خلال آخر خمس سنوات"
    BLOCK_DATA_HERO_2_EN = "Number Of Employees"
    BLOCK_DATA_HERO_2_AR = "إجمالي الموظفين"
    BLOCK_DATA_HERO_3_EN = "Number Of Establishments"
    BLOCK_DATA_HERO_3_AR = "إجمالي المنشآت"

    EXPLORE_BUTTON_EN = "Explore"
    EXPLORE_BUTTON_AR = "ابدأ التصفح"


@dataclasses.dataclass
class InsightBlock:
    TITLE_EN = "Find actionable insights"
    TITLE_AR = "تصفح واعثر على احصائيات تهمك"
    DESCRIPTION_EN = "Accessible and actionable insights with key takeaways, graphs, and reports"
    DESCRIPTION_AR = "احصائيات وتقارير عن سوق العمل السعودي"
    SLIDER_LIST_DESCRIPTIONS_EN = [
        "Decrease of the number of employees\nfor last 6 months",
        "Average Age",
        "Decrease of the number of establishments\nfor last 6 months",
        "Decrease of women laborforce\nfor last 6 months",
    ]
    SLIDER_LIST_DESCRIPTIONS_AR = [
        "النقص في أعداد الموظفين\nخلال آخر ستة أشهر",
        "متوسط الأعمار",
        "النقص في أعداد المنشآت\nخلال آخر ستة أشهر",
        "النقص في توظيف النساء\nخلال آخر ستة أشهر",
    ]


@dataclasses.dataclass
class SolutionBlock:
    TITLE_EN = "Solutions for smart decision making"
    TITLE_AR = "حلول لتمكين اتخاذ القرار"
    DESCRIPTION_EN = (
        "Comprehensive, accurate information from every angle to give the most complete,"
        " nuanced, up-to-date picture of the labor market possible."
    )
    DESCRIPTION_AR = (
        "معلومات شاملة ودقيقة من زوايا مختلفة لإعطاء الصورة الكاملة والمحدثة عن سوق العمل"
    )
    ITEMS_EN = ["Companies", "Employees", "Policy makers", "Foreign entities", "Researches"]
    ITEMS_AR = ["المنشآت", "الموظفين", "متخذي القرار", "الجهات الخارجية", "الباحثين"]
    ITEMS_DESCRIPTION_EN = [
        "Get insights into the current state of the labor market in Saudi Arabia and check out your"
        " sector stats",
        "Get information on workforce and establishments statistics, and compare"
        " between the different sectors",
        "Measure impact of the policy changes."
        " Monitor changes in market, Market overview. Empower data-based decision making",
        "360 degree overview of human capital of KSA. Check out biggest and smallest sectors by"
        " employees or establishments count.",
        "Get access to data, different indicators, and "
        "insights. Send a request to order a custom research",
    ]
    ITEMS_DESCRIPTION_AR = [
        "اطلع على إحصائيات وتوجهات سوق العمل السعودي",
        "احصل على إحصائيات القوى العاملة والمنشآت وقارن مختلف الأنشطة",
        "قياس تأثير السياسات ومتابعة التغيرات في السوق وتمكين صنع القرار المستند على البيانات",
        "اطلع على إحصائيات وتوجهات سوق العمل السعودي",
        "اطلع على البيانات والمؤشرات والاحصائيات المختلفة. راسلنا لطلب بحث مخصص",
    ]


@dataclasses.dataclass
class TrendingStatsBlock:
    TITLE_EN = "Qiwa Data"
    TITLE_AR = "قوى بيانات"
    DESCRIPTION_EN = [
        "Qiwa Data is a platform for labor market insights. It provides strategic data on current"
        " industry trends that impact your business, overview of key indicators and metrics, essential"
        " for making decisions about human capital."
    ]
    DESCRIPTION_AR = [
        "قوى بيانات هي منصة لإحصائيات سوق العمل، توفر بيانات إستراتيجية حول اتجاهات"
        " سوق العمل الحالية ونظرة عامة عن المؤشرات والمقاييس الرئيسية لمساعدة الباحثين ومتخذي القرار."
    ]
    EXPLORE_STATS_TITLE_EN = "Explore trending stats:"
    EXPLORE_STATS_TITLE_AR = "اكتشف آخر التقارير:"

    EXPLORE_CARD_TITLE_EN = "Market Overview"
    EXPLORE_CARD_TITLE_AR = "نظرة عامة على سوق العمل"


@dataclasses.dataclass
class TrustBlock:
    TITLE_EN = "Data you can trust"
    TITLE_AR = "بيانات موثوقة"
    DESCRIPTION_EN = "Scientific approach to gathering and working with data among different sectors. Up to date."
    DESCRIPTION_AR = "طرق منهجية لجمع وعرض البيانات الموثوقة والحديثة"
    TRUST_INFO_EN = ["Sectors", "Users of Qiwa", "The volume of historical data"]
    TRUST_INFO_AR = ["نشاط اقتصادي", "عدد المستخدمين في منصة قوى", "عمر البيانات التاريخية"]
    PROVIDED_TITLE_EN = ["DATA", "PROVIDED BY"]
    PROVIDED_TITLE_AR = ["البيانات", "بواسطة"]


@dataclasses.dataclass
class ElementType:
    IMAGE = "image"
    TEXT = "text"


@dataclasses.dataclass
class CustomizeModal:
    CRITERIA = "te"
    INVALID_CRITERIA = "tenn"
    SEARCH_RESULT = [
        "Water supply; sewerage, waste management and remediation activities",
        "Real estate activities",
        "Professional, scientific and technical activities",
        "Arts, entertainment and recreation",
        "Electricity, gas, steam and air conditioning supply",
    ]
    NO_RESULTS = "No results found"
    SELECT_ALL_OPTION = "Select all"
    SELECT_ALL_CRITERIA = "All"
    CATERING_OPTION = "Construction"
    FINANCE_OPTION = "Manufacturing"


@dataclasses.dataclass
class ContactUs:
    TITLE_EN = "Contact us"
    TITLE_AR = "تواصل معنا"
    FIELD_NAMES_EN = ["Full Name", "Email", "Company (optional)"]
    FIELD_NAMES_AR = ["الاسم الكامل", "البريد الإلكتروني", "المنشأة (إختياري)"]
    TITLE_SUCCESS_EN = "Thank you for getting in touch with us!"
    TITLE_SUCCESS_AR = "شكرًا لتواصلك معنا!"
    DESCR_SUCCESS_EN = (
        "Our team will review your message and respond as soon as possible. In the meantime, "
        "feel free to browse our website and learn more about what we have to offer."
        " We look forward to connecting with you soon!"
    )
    DESCR_SUCCESS_AR = (
        "سنراجع رسالتك ونقوم بالرد عليك في أقرب وقت ممكن"
        "، لا تتردد في تصفح الموقع ومعرفة المزيد عن ما نقدمه. نتطلع إلى التواصل معك قريبًا!"
    )
    VALIDATION_ALERTS_EN = [
        "Please enter your full name.",
        "Please enter valid email.",
        "Please provide a reason for contacting us with a minimum of 30 characters.",
    ]
    VALIDATION_ALERTS_AR = [
        "فضلًا أدخل اسمك الكامل",
        "فضلًًا أدخل بريد إلكترني صحيح",
        "فضلًا اكتب سبب تواصلك معنا بحيث لا تقل رسالتك عن 30 حرف.",
    ]
    SEND_BUTTON_EN = "Send"
    SEND_BUTTON_AR = "إرسال"
    BACK_BUTTON_EN = "Back to Home"
    BACK_BUTTON_AR = "العودة للخلف"

    """Contact us block"""
    BLOCK_TITLE_EN = "Custom request?"
    BLOCK_TITLE_AR = "هل لديك طلب خاص أو اقتراح؟"
    DESCRIPTION_EN = "If you want to have a custom research or get access to pro functionality, please contact us."
    DESCRIPTION_AR = "تواصل معنا اذا كنت ترغب في طلب إحصائيات أو بحوث مخصصة"
    BUTTON_EN = "Contact us"
    BUTTON_AR = "تواصل معنا"


@dataclasses.dataclass
class Variables:
    AUTOTEST = "Autotest"
    EMAIL = "autotest@autotest.com"
    EMAIL_WITHOUT_AT = "autotest.com"
    EMAIL_WITHOUT_DOT = "autotest@testcom"
    EMAIL_WITHOUT_PREFIX = "@test.com"
    EMAIL_WITHOUT_DOMAIN = "autotest"
    COMPANY = "Autotest Company"
    INACTIVE_STATUS = "inactive"
    ACTIVE_STATUS = "active"
    EMPTY = ""

    @staticmethod
    def generate_string(length):
        characters = "Autotest_-!@#$%^&*()_1234567890-=<>/.,';"
        generated_string = "".join(random.choice(characters) for _ in range(length))
        return generated_string


@dataclasses.dataclass
class Localization:
    EN_LOCAL = "English"
    AR_LOCAL = "العربية"


@dataclasses.dataclass
class AboutUs:
    HERO_TITLE_EN = "About us"
    HERO_TITLE_AR = "عن قوى بيانات"
    HERO_DESCRIPTION_EN = (
        "Qiwa Data was built to help leverage data and labor market insights for better decisions"
        " about human capital."
    )
    HERO_DESCRIPTION_AR = (
        "بدأنا قوى بيانات لنساعد"
        " في الاستفادة من البيانات ورؤى سوق العمل لاتخاذ قرارات أفضل بشأن الموارد البشرية."
    )

    MISSION_TITLE_EN = "Our mission"
    MISSION_TITLE_AR = "مهمتنا"
    MISSION_CARD_TITLE_EN = [
        "To be a key partner for Decision Makers",
        "To be an advisor for Business Sustainability",
    ]
    MISSION_CARD_TITLE_AR = [
        "أن نكون شريكًا رئيسيًا لصناع القرار",
        "أن نكون المستشار الأول لاستدامة الأعمال",
    ]
    MISSION_CARD_DESCRIPTION_EN = [
        "Qiwa Data allows for deriving actionable insights from data, which may be utilized "
        "to inform decision-making and strategy creation.",
        "Qiwa Data visualizes data in a way that uncovers insights from complex data sets"
        " and makes it accessible and actionable.",
    ]
    MISSION_CARD_DESCRIPTION_AR = [
        "يتيح قوى بيانات استخلاص رؤى قا"
        "بلة للتنفيذ من البيانات، والتي يمكن استخدامها لصنع القرار والاستراتيجيات.",
        "نقوم في قوى بيانات بتصور البيانات بطريقة"
        " تكشف عن الرؤى من مجموعات البيانات المعقدة وتجعلها سهلة الوصول وقابلة للتنفيذ.",
    ]
    BENEFITS_TITLE_EN = "Our benefits"
    BENEFITS_TITLE_AR = "مميزاتنا"
    BENEFITS_CARD_TITLE_EN = [
        "Actionable insights",
        "Trend analysis",
        "Labor market intelligence",
        "Data you can trust",
    ]
    BENEFITS_CARD_TITLE_AR = ["رؤى تطلعيّة", "تحليل الاتجاه", "بيانات سوق العمل", "أرقام تثق بها"]
    BENEFITS_CARD_DESCRIPTION_EN = [
        "50 indicators for different segments. Accessible and actionable insights with"
        " key takeaways, graphs, and reports",
        "Trend analysis and forecasting based on historical data.",
        "Comprehensive labor market overview.",
        "A scientific approach to gathering and analyzing data across various sectors.",
    ]
    BENEFITS_CARD_DESCRIPTION_AR = [
        "أكثر من 50 مؤشرًا"
        " لمختلف القطاعات، ورؤى تطلعية قابلة للتنفيذ مع رسوم بيانية وتقارير احصائية",
        "تحليل الاتجاه والتنبؤ على أساس البيانات التاريخية",
        "نظرة شاملة على سوق العمل",
        "نهج علمي لجمع وتحليل البيانات من مختلف القطاعات.",
    ]
    BELIEVE_TITLE_EN = "What we believe in"
    BELIEVE_TITLE_AR = "ما نؤمن به"
    BELIEVE_CARD_TITLE_EN = [
        "Transparency",
        "Healthy competition",
        "Brand reputation",
        "Curiosity, knowledge & learning",
        "Influence/action",
        "",
    ]
    BELIEVE_CARD_TITLE_AR = [
        "الشفافية",
        "المنافسة الصحية",
        "سمعة العلامة",
        "الفضول، والمعرفة، والتعلم",
        "التأثير",
        "",
    ]
    BELIEVE_CARD_DESCRIPTION_EN = [
        "Transparency breeds trust, helps make the right decisions, and drives significant "
        "progress.",
        "Comprehensive labor market overview",
        "Trust, credibility, and loyalty are the pillars of our brand.",
        "We cherish the culture of curiosity to power ongoing learning at the heart of "
        "future success.",
        "The knowledge that brings actionable insights and impact.",
        "",
    ]
    BELIEVE_CARD_DESCRIPTION_AR = [
        "تولد الشفافية الثقة، وتساعد في اتخاذ القرارات الصحيحة والتقدم العظيم.",
        "نظرة شاملة على سوق العمل",
        "الثقة، والمصداقية، والإخلاص هي أعمدتنا في قوى بيانات",
        "نعتز بسِمة الفضول وندعم التعلم المستمر في المستقبل.",
        "المعرفة التي تجلب رؤى تطلعية ذات تأثيرعالي",
        "",
    ]
    QIWA_SA_TITLE_EN = "Qiwa.sa"
    QIWA_SA_TITLE_AR = "Qiwa.sa"
    QIWA_SA_DESCRIPTION_EN = [
        "Qiwa platform is an electronic platform that provides the Ministry of Human Resources"
        " and Social Development services and solutions to enhance the electronic services"
        " provided to the labor sector.",
        "Qiwa Data is a part of Qiwa platform, which empowers Qiwa with statistics and data"
        " analysis.",
    ]
    QIWA_SA_DESCRIPTION_AR = [
        "منصة قوى هي منصة إلكترونية تزود وزارة الموارد البشرية "
        "والتنمية الاجتماعية بالخدمات والحلول لتعزيز الخدمات الإلكترونية المقدمة لقطاع العمل.",
        "قوى بيانات هي جزء من منصة قوى ، والتي تمكن قوى من خلال الإحصائيات وتحليل البيانات.",
    ]
    QIWA_VISIT_TITLE_EN = "Visit Qiwa:"
    QIWA_VISIT_TITLE_AR = "قم بزيارة منصة قوى"
    QIWA_VISIT_LINK_EN = ["Website", "LinkedIn", "Twitter"]
    QIWA_VISIT_LINK_AR = ["الموقع الإلكتروني", "LinkedIn", "Twitter"]


@dataclasses.dataclass
class SubscribeBlock:
    TITLE_EN = "Subscribe to the monthly Newsletter"
    TITLE_AR = "تابع التحديثات والتقارير الجديدة"
    DESCRIPTION_EN = (
        "Keep up to date with our latest news and analysis by subscribing"
        " to our regular newsletter"
    )
    DESCRIPTION_AR = "سجل بريدك الإلكتروني لمتابعة التحديثات والتقارير الجديدة"
    PLACEHOLDER_EN = "Enter your e-mail address"
    PLACEHOLDER_AR = "ادخل بريدك الإلكتروني"
    BUTTON_EN = "Subscribe"
    BUTTON_AR = "تسجيل"
    SUCCESS_MESSAGE_EN = (
        "You have successfully subscribed to our newsletter!"
        " Thank you for joining our community."
    )
    SUCCESS_MESSAGE_AR = "لقد تابعت نشرتنا البريدية بنجاح! شكرا لانضمامك إلى مجتمعنا."


@dataclasses.dataclass
class AllSectors:
    SHEET = "Sectors"

    HERO_TITLE_EN = "Sectors"
    HERO_TITLE_AR = "نشاط اقتصادي"
    SEARCH_PLACEHOLDER_EN = "Search"
    SEARCH_PLACEHOLDER_AR = "بحث"
    SEARCHING_CRITERIA = "ال"
    SEARCH_ITEMS_EN = [
        "أندية الخيل والفروسية",
        "أنشطة البريد",
        "إسناد الموظفين السعوديين",
        "الإنتاج الزراعي والحيواني وخدماتها واندية الفروسية",
        "الايواء والترفيه والسياحة",
    ]

    SEARCH_ITEMS_AR = [
        "الباب ( س ) : الإدارة العامة والدفاع , الضمان الاجتماعي الالزامي",
        "الباب ( أ ): الزراعة والحراجة وصيد الأسماك",
        "الباب ( ب ): التعدين واستغلال المحاجر",
        "الباب ( ج ): الصناعة التحويلية",
        "الباب ( ح ) : النقل والتخزين",
    ]
    NO_RESULTS_EN = ["No results found"]
    NO_RESULTS_AR = ["لم يتم العثور على نتائج"]

    ECONOMIC_ACTIVITIES_EN = "Economic Activities"
    ECONOMIC_ACTIVITIES_AR = "الأنشطة الاقتصادية"
    NITAQAT_ACTIVITIES_EN = "Nitaqat Activities"
    NITAQAT_ACTIVITIES_AR = "الأنشطة حسب تصنيف نطاقات"
    LOAD_MORE_SECTORS_EN = "Load more sectors"
    LOAD_MORE_SECTORS_AR = "عرض كل الأنشطة"

    SECTORS_EN = None
    SECTORS_AR = None

    """Explore by sector block"""
    TITLE_EN = "Explore by sector"
    TITLE_AR = "تصفح حسب النشاط الاقتصادي"
    SECTORS_NAME_EN = [
        "أندية الخيل والفروسية",
        "أنشطة البريد",
        "إسناد الموظفين السعوديين",
        "الإنتاج الزراعي والحيواني وخدماتها واندية الفروسية",
        "الايواء والترفيه والسياحة",
        "البنية التحتية لتقنية المعلومات",
        "البنية التحتية للاتصالات",
        "التشغيل والصيانة",
    ]
    SECTORS_NAME_AR = [
        "إسناد الموظفين السعوديين",
        "الإنتاج الزراعي والحيواني وخدماتها واندية الفروسية",
        "الايواء والترفيه والسياحة",
        "البنية التحتية لتقنية المعلومات",
        "البنية التحتية للاتصالات",
        "التشغيل والصيانة",
        "التشغيل والصيانة لتقنية المعلومات",
        "التشغيل والصيانة للاتصالات",
    ]


@dataclasses.dataclass
class Sector:
    URL = "https://data.qiwa.info/sector/{0}?type=NITAQAT&colorIndex=0"

    """Finance sector chart"""
    TITLE_EN = "Compare, find, forecast"
    TITLE_AR = "قارن، ابحث، وتنبأ"
    DESCRIPTION_EN = "Trend analysis and forecasting based on historical data"
    DESCRIPTION_AR = "تحليل اتجاهات سوق العمل والاطلاع على البيانات التاريخية"
    EXPLORE_BUTTON_EN = "Explore Finance sector"
    EXPLORE_BUTTON_AR = "استكشف القطاع المالي"
    TITLE_HEADER_EN = "Number of Employees in Finance sector"
    TITLE_HEADER_AR = "عدد الموظفين في القطاع المالي"


@dataclasses.dataclass
class EstablishmentsChart:
    PICK_UNIFIED_OPTION = "pick unified option"
    PICK_ENTITIES_OPTION = "pick entities option"


@dataclasses.dataclass
class EmployeesChart:
    GO_TO_GENDER_TAB = "navigate to gender tab"
    LINE_CHART = "Line Chart"
    DOUGHNUT_CHART = "Doughnut Chart"
    CALENDAR_OPTIONS = ["Last quarter", "Last year", "All time", "Custom period"]
    LAST_QUARTER = "Last quarter"
    LAST_YEAR = "Last year"
    ALL_TIME = "All time"
    CUSTOM_PERIOD = "Custom period"


@dataclasses.dataclass
class WorkforceChart:
    ALL_SECTORS = "All Sectors"


@dataclasses.dataclass
class Reports:
    TITLE_EN = "Reports"
    TITLE_AR = "التقارير"
    TOPIC_TITLES_EN = ["Indicators", "Saudi Economy", "Economic research topic"]
    TOPIC_TITLES_AR = ["Indicators ar", "Saudi Economy ar", "Economic research topic ar"]
    TOPIC_DESCRIPTIONS_EN = [
        "Market Overview",
        "Employee Turnover - 2023",
        "Employee Tenure - 2023",
        "Workplace environment report - 2023",
        "Establishments and labor structure report - 2023",
        "Establishment size report - 2023",
        "Disaggregating the Saudi Employment Rate into its components - 2023",
        "Gender productivity in the Saudi economy - 2023",
        "The seven level of Saudi unemployment - 2023",
        "Establishment size report - 2023",
    ]
    TOPIC_DESCRIPTIONS_AR = [
        "Market Overview",
        "Employee Turnover - 2023",
        "Employee Tenure - 2023",
        "Workplace environment report - 2023",
        "Establishments and labor structure report - 2023",
        "Establishment size report - 2023",
        "Disaggregating the Saudi Employment Rate into its components - 2023",
        "Gender productivity in the Saudi economy - 2023",
        "The seven level of Saudi unemployment - 2023",
        "Establishment size report - 2023",
    ]


@dataclasses.dataclass
class PrivacyPolicy:
    SHEET = "Privacy policy"


@dataclasses.dataclass
class Admin:
    LOGIN = "qiwa-data"
    PASSWORD = "qiwa-data"
    INVALID_LOGIN = "invalid-qiwa-data"
    INVALID_PASSWORD = "invalid-qiwa-data"
    VALIDATION_MESSAGE = "Unrecognized username or password. Forgot your password?"
    LOGIN_PAGE = "Log in"
    AUTOMATION = "automation"
    AUTOMATION_UPPER_CASE = "Automation"
    AUTOMATION_EDIT = "automation-edited"
    TABS = ["Content", "Reports\n(active tab)", "Blocks", "Takeaway Sections", "Files"]
    FILTERS = ["Title", "Published status", "Language", "Category"]
    REPORT_CATEGORY_COLUMNS = [
        "Title",
        "Likes",
        "Sharing",
        "Language",
        "Status",
        "Author",
        "Updated\nSort ascending",
        "Copy Link",
        "Operations",
    ]
    LANGUAGES = ["English (Original language)", "Arabic"]
    MODAL_WARNING = "Are you sure you want to delete the content item {0}?"
    PUBLISHED_NAME = "Published"
    PUBLISHED = "1"
    UNPUBLISHED = "2"
    ENGLISH_FILTER = "en"
    ARABIC_FILTER = "ar"
    CHANGE_CATEGORY_SUCCESS_MESSAGE = "Node {0} category changed to {1}."
    VALIDATION_TITLE = "The title of the takeaway section cannot contain special symbols."
    VALIDATION_CONTENT = "The text is too long: the limit is 2000 characters."
    AUTOMATION_AR = "أتمتة"
    CREATE_REPORT_TITLE = "Create Report"
    CREATE_REPORT_REQUIRED_FIELDS = ["Report name", "Duration Read", "Add a new file"]
    ADD_NEW_TERM = "Add new taxonomy term"
    ADD_EXISTING_TERM = "Add existing taxonomy term"
    BLOCKS_DROPDOWN_TITLE = "Chart"
    ADD_NEW_BLOCK = "Add new content block"
    BROWSER_VALIDATION = "Please fill out this field."
    BROWSER_VALIDATION_DURATION = "Value must be greater than or equal to 1."
    ERROR_MESSAGE = "Error message"
    IMAGE_VALIDATION_ERROR = (
        "The selected file {0} cannot be uploaded."
        " Only files with the following extensions are allowed: png, gif, jpg, jpeg, webp."
    )
    IMAGE_RESOLUTION_ERROR = (
        "The specified file {0} could not be uploaded.\nThe image is too small. "
        "The minimum dimensions are 1280x720 pixels and the image size is 640x426 pixels."
    )
    PNG = "admin_portal_test_attach.png"
    PNG_640 = "admin_portal_test_attach_640×426.png"
    GIF = "admin_portal_test_attach.gif"
    GIF_640 = "admin_portal_test_attach_640×426.gif"
    JPG = "admin_portal_test_attach.jpg"
    JPG_640 = "admin_portal_test_attach_640×426.jpg"
    JPEG = "admin_portal_test_attach.jpeg"
    JPEG_640 = "admin_portal_test_attach_640×426.jpeg"
    WEBP = "admin_portal_test_attach.webp"
    WEBP_640 = "admin_portal_test_attach_640×426.webp"
    ICO = "admin_portal_test_attach.ico"
    TXT = "admin_portal_test_attach.txt"
    DOC = "admin_portal_test_attach.doc"
    PDF = "admin_portal_test_attach.pdf"
    CHART = "chart"
    IMAGE = "image"
    IMAGE_PARAGRAPH = "image-paragraph"
    NUMBER = "number"
    CURRENCY = "currency"
    PERCENTAGE = "percentage"
    YELLOW = (252, 182, 20)
    BOLD = "Bold (Ctrl+B)"
    ITALIC = "Italic (Ctrl+I)"
    UNDERLINE = "Underline (Ctrl+U)"
    STRIKETHROUGH = "Strikethrough (Ctrl+Shift+X)"
    SUBSCRIPT = "Subscript"
    SUPERSCRIPT = "Superscript"
    HYPER_LINK = "Link (Ctrl+K)"
    ALIGN_LEFT = "Align left"
    ALIGN_RIGHT = "Align right"
    ALIGN_CENTER = "Align center"
    ALIGN_JUSTIFY = "Justify"
    GOOGLE_LINK = "https://www.google.com/"
