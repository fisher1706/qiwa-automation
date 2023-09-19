import allure
import jmespath

import config
from src.api.assertions.response_validator import ResponseValidator


class WeqApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.total_final_index = None
        self.api = api
        self.indexes = None
        self.list_for_calculation = []
        self.d_value_lists = []

    @allure.step("GET /lmi-admin/surveys/indexes :: get indexes")
    def get_indexes(self, cookies=None, expect_code=200):
        response = self.api.get(
            url=self.url, endpoint="/lmi-admin/surveys/indexes", cookies=cookies
        )
        validator = ResponseValidator(response)
        validator.check_status_code(name="GET /lmi-admin/surveys/indexes", expect_code=expect_code)
        self.indexes = response.json()
        return self

    @allure.step("I get Total final index")
    def get_total_final_index(self, cookies=None):
        self.get_indexes(cookies)
        total_final_index = jmespath.search("[*].total_retail[*].total_final_index", self.indexes)
        self.total_final_index = round(total_final_index[0][0], 2)

    @allure.step("POST /lmi-admin/surveys/indexes/calculate/start :: perform calculation")
    def post_calculate_indexes(self, expect_code=200, expect_schema="calculation_indexes.json"):
        response = self.api.post(
            url=self.url, endpoint="/lmi-admin/surveys/indexes/calculate/start"
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /lmi-admin/surveys/indexes/calculate/start", expect_code=expect_code
        )
        validator.check_response_schema(schema_name=expect_schema)
        for _ in range(3):
            self.get_indexes()
            if self.indexes:
                break
        return self

    def get_list_for_calculation(self, survey_details, parse_xls_result):
        for question in survey_details["data"]["attributes"]["survey_questions"]:
            question_dict = {}
            dimension_dict = {}
            if question["dimension"]["name"] is None:
                continue
            answers_list = []
            for answer in parse_xls_result[question["title"]]:
                for question_choice in question["question_choices"]:
                    if question_choice["title"] == str(answer):
                        answers_list.append(float(question_choice["weight"]))
            average_answer = round(sum(answers_list) / float(len(answers_list)), 2)
            question_dict[question["title"]] = float(question["weight"])
            question_dict["max_question_weight"] = float(question["max_answer_score"])
            question_dict["answers_average"] = average_answer
            question_dict["dimension"] = question["dimension"]["name"]
            for dimension in survey_details["data"]["attributes"]["dimensions"]:
                if dimension["weight"] == 0:
                    continue
                if dimension["name"] == question_dict["dimension"]:
                    dimension_dict[dimension["name"]] = [question_dict]
                    dimension_dict["dimensions_weight"] = float(dimension["weight"])
            self.list_for_calculation.append(dimension_dict)
        return self.list_for_calculation

    @staticmethod
    def parse_question(question):
        (name, question_weight) = list(question.items())[0]
        answers_average = question["answers_average"]
        max_question_weight = question["max_question_weight"]
        return [name, question_weight, max_question_weight, answers_average]

    @staticmethod
    def parse_dimension(dimension):
        (name, questions) = list(dimension.items())[0]
        dimensions_weight = dimension["dimensions_weight"]
        return [name, questions, dimensions_weight]

    def handle_dimension(self, dimension):
        (_, questions, dimensions_weight) = self.parse_dimension(dimension)
        qw_d = 0
        d_value = 0
        for question in questions:
            (_, question_weight, max_question_weight, answers_average) = self.parse_question(
                question
            )
            qw_d = question_weight / dimensions_weight * 100
            question_dimension_index = (answers_average / max_question_weight) * qw_d
            d_value = d_value + (question_dimension_index * dimensions_weight / 100)
        self.d_value_lists.append(d_value)
        return qw_d

    def handle_dimensions(self, dimensions):
        score = 0
        for dimension in dimensions:
            score = score + self.handle_dimension(dimension)
        return score
