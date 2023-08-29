from enum import Enum

import config


class UrlForBreadcrumbs(Enum):
    E_SERVICES_URL = config.settings.qiwa_spa_url + "/company/e-services"
    DELEGATION_DASHBOARD_URL = config.settings.qiwa_delegation_url
