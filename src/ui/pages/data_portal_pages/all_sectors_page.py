from selene import be, query
from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss


class AllSectorsPage:
    HERO_TITLE = s('//section[@class="container sectors"]//h1')
    SEARCH_FIELD = s('//div[@class="input-wrapper"]//input')
    SEARCH_RESULT = ss('//div[contains(@class, "body-02-paragraph")]')
    SECTORS_LIST = s(".sectors-list ")
    CLEAR_RESULT_BUTTON = s(".clear-icon-wrapper")

    ECONOMIC_ACTIVITIES = s('(//section[@class="container sectors"]//div[2]//div)[1]')
    NITAQAT_ACTIVITIES = s('(//section[@class="container sectors"]//div[2]//div)[2]')
    SERVICE_LINK = s('//a[@class="sector-card-link"]')
    SECTOR_CARD = s('//div[@class="sectors-list mt-6 sm-mt-8 xl-mt-6 d-flex flex-wrap"]//img')
    SECTOR_TITLE = s('//div[@class="sectors-list mt-6 sm-mt-8 xl-mt-6 d-flex flex-wrap"]//span')

    """Explore by sector block"""
    TITLE = s('//section[@id="explore-sector"]/div/div[2]')
    SECTORS_CARD = ss(
        '//div[@class="sector-card body-02-highlight md-body-01-highlight relative simple-card"]/span'
    )
    VIEW_ALL_SECTORS_BUTTON = s('//a[@class="button button-regular button-secondary"]')

    def check_matched_items(self, target_items):
        self.SECTORS_LIST.should(be.visible)
        search_result = []
        for item in self.SEARCH_RESULT:
            search_result.append(item.get(query.text))
        assert search_result == target_items

    def clear_search_field(self):
        self.CLEAR_RESULT_BUTTON.click()
        self.SEARCH_FIELD.should(have.value(""))

    @staticmethod
    def pick_activities(activities_type):
        activities_type.should(be.enabled)
        activities_type.click()

    def check_elements_on_the_page(self, elements, list_text):
        self.SECTORS_LIST.should(be.visible)
        elements_list = []
        for element in elements:
            elements_list.append(element.get(query.text))
        assert elements_list == list_text

    def perform_searching(self, search_criteria, target_items):
        self.SEARCH_FIELD.set_value(search_criteria).click()
        self.check_matched_items(target_items)
        self.clear_search_field()
