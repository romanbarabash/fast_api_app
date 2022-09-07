import jsonschema
from hamcrest import assert_that, equal_to, contains_string
from requests import Session


class BaseService:

    def __init__(self, client, headers):
        self.client: Session = client
        self.headers = headers


class AssertResponse:

    def __init__(self, response):
        self.response = response

    def status_code_is(self, code: int):
        assert_that(self.response.status_code, equal_to(code))
        return self

    def has_items(self, obj_items_qty: int):
        assert_that(len(self.response.json()), equal_to(obj_items_qty))
        return self

    def value_equals(self, actual_response_item, expected_item, is_contains=False):
        if is_contains:
            assert_that(self.response.json()[actual_response_item]), contains_string((expected_item))
        else:
            assert_that(self.response.json()[actual_response_item]), equal_to(expected_item)
        return self

    def validate_schema(self, expected_schema):
        jsonschema.validate(self.response.json(), expected_schema)
        return self
