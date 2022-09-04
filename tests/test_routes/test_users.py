import jsonschema

from backend.models.users import UserModelAPI
from tests.services.json_schemas.user_schemas import user_schema


def test_create_user(get_user_service):
    user_service = get_user_service
    user_model = UserModelAPI.create()

    response = user_service.create_user(user=user_model)

    assert response.status_code == 200
    assert response.json()["email"] == user_model.email
    assert response.json()["is_active"] == True

    jsonschema.validate(response.json(), user_schema)
