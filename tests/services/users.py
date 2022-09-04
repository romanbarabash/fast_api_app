from backend.models.users import UserModelAPI
from tests.services.base import BaseService


class UserService(BaseService):

    def __init__(self, client, headers):
        super().__init__(client, headers)

    def create_user(self, user: UserModelAPI):
        path = '/users/'
        return self.client.post(url=path, data=user.to_json())
