import random

from faker import Faker
from sqlalchemy.orm import Session

from backend.api.api_models.users import UserCreateModel
from backend.db.queries.users import create_new_user

fake = Faker(['en-US'])


def create_random_owner(db: Session):
    user_schema = UserCreateModel(username=f'{fake.first_name()} {fake.last_name()}',
                                  email=fake.ascii_safe_email(),
                                  password=random.randint(100000, 9999999))
    user = create_new_user(user=user_schema, db=db)
    return user
