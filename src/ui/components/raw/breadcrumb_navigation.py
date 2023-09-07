from __future__ import annotations

from selene import browser
from selene.core.entity import Element


class BreadcrumbNavigation:
    breadcrumbs = browser.all('[aria-label="Breadcrumb"] li')

    def breadcrumb(self, index: int) -> Element:
        return self.breadcrumbs.element(index - 1)
