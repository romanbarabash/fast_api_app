from backend.models.users import UserModelAPI


def test_create_user(client):
    user = UserModelAPI.create().to_json()
    response = client.post(url="/users/", data=user)

    assert response.status_code == 200
    assert response.json()["email"] in user
    assert response.json()["is_active"] == True
