from backend.models.users import UserModelAPI
from tests.services.base import BaseService


class UserService(BaseService):

    def __init__(self, client, headers):
        super().__init__(client, headers)

    def create_user(self, user: [UserModelAPI, None]):
        path = '/users/'
        payload = user.to_json() if user else {}
        return self.client.post(url=path, data=payload)
