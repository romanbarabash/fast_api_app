from backend.models.users import UserModelAPI


class UserService:

    def __init__(self, client):
        self.client = client

    def create_user(self, user: UserModelAPI):
        path = '/users/'
        return self.client.post(url=path, data=user.to_json())
