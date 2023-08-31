from enum import Enum

import config


class UrlForBreadcrumbs(Enum):
    E_SERVICES_URL = config.qiwa_urls.spa + "/company/e-services"
    DELEGATION_DASHBOARD_URL = config.qiwa_urls.delegationservice
