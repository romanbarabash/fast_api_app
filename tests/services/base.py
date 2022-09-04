import jsonschema


class BaseService:

    def __init__(self, client, headers):
        self.client = client
        self.headers = headers


class AssertResponse:

    def __init__(self, response):
        self.response = response

    def status_code_is(self, code: int):
        assert self.response.status_code == code
        return self

    def has_items(self, obj_items_qty: int):
        assert len(self.response.json()) == obj_items_qty
        return self

    def value_matcher(self, actual_response_item, expected_item):
        assert self.response.json()[actual_response_item] == expected_item
        return self

    def validate_schema(self, expected_schema):
        jsonschema.validate(self.response.json(), expected_schema)
        return self
