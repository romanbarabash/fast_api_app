import random

import pytest

from backend.models.users import UserModelAPI
from backend.utils import fake
from tests.services.base import AssertResponse
from tests.services.json_schemas.login_schemas import token_schema


@pytest.fixture
def create_user(get_user_service):
    user_model = UserModelAPI.create()
    user_response = get_user_service.create_user(user=user_model)
    return user_model, user_response


@pytest.mark.possitive
def test_login_with_token(get_login_service, create_user):
    login_service = get_login_service
    user_model, user_response = create_user

    response = login_service.login_user(username=user_model.email,
                                        password=user_model.password)

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(2) \
        .validate_schema(token_schema)


@pytest.mark.negative
def test_login_incorrect_username(get_login_service, create_user):
    login_service = get_login_service
    user_model, user_response = create_user

    response = login_service.login_user(username=fake.last_name,
                                        password=user_model.password)

    AssertResponse(response) \
        .status_code_is(401) \
        .value_equals(actual_response_item='detail', expected_text='Incorrect username or password.')


@pytest.mark.negative
def test_login_incorrect_password(get_login_service, create_user):
    login_service = get_login_service
    user_model, user_response = create_user

    response = login_service.login_user(username=user_model.email,
                                        password=str(random.randint(1_000_000, 9_999_999)))

    AssertResponse(response) \
        .status_code_is(401) \
        .value_equals(actual_response_item='detail', expected_text='Incorrect username or password.')
