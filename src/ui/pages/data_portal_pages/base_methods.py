from selene import have, query


class BaseMethods:
    @staticmethod
    def check_element_on_the_page(element, text):
        element.should(have.text(text))

    @staticmethod
    def check_elements_on_the_page(elements, list_text):
        elements_list = []
        for element in elements:
            elements_list.append(element.get(query.text))
        assert elements_list == list_text, f"{elements_list}\n{list_text}"


base_methods = BaseMethods()
