from tests.services.base import AssertResponse


def test_login_with_token(get_login_service, create_user):
    login_service = get_login_service
    user = create_user

    response = login_service.login_user(username=user.get('username'), password=user.get('password'))
    # TODO - grab the user password

    AssertResponse(response) \
        .status_code_is(200)
