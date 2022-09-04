from backend.models.users import UserModelAPI
from tests.services.base import AssertResponse
from tests.services.json_schemas.user_schemas import user_schema


def test_create_user(get_user_service):
    user_service = get_user_service
    user_model = UserModelAPI.create()

    response = user_service.create_user(user=user_model)

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(4) \
        .value_matcher(actual_response_item="email", expected_item=user_model.email) \
        .value_matcher(actual_response_item="is_active", expected_item=True) \
        .validate_schema(user_schema)
