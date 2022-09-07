from tests.services.base import BaseService


class LoginService(BaseService):

    def __init__(self, client, headers):
        super().__init__(client, headers)

    def login_user(self, username, password):
        path = '/login/token'
        payload = {'username': username, 'password': password}
        return self.client.post(url=path, data=payload)
