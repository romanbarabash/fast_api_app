import random

from faker import Faker
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from backend.db.queries.login import get_user
from backend.db.queries.users import create_new_user
from backend.models.users import UserModelAPI

fake = Faker(['en-US'])


def create_random_owner(db: Session):
    user_schema = UserModelAPI(username=f'{fake.first_name()} {fake.last_name()}',
                               email=fake.ascii_safe_email(),
                               password=random.randint(100000, 9999999))
    user = create_new_user(user=user_schema, db=db)
    return user


def user_authentication_headers(client: TestClient, email: str, password: str):
    data = {"username": email, "password": password}
    r = client.post("/login/token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_email(client: TestClient, email: str, db: Session):
    password = "random-passW0rd"
    user = get_user(username=email, db=db)
    if not user:
        new_user = UserModelAPI(username=email, email=email, password=password)
        create_new_user(user=new_user, db=db)
    return user_authentication_headers(client=client, email=email, password=password)
