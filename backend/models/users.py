import random
from typing import Optional

from pydantic import EmailStr

from backend.models.base import Model, fake


class UserModelAPI(Model):
    username: str
    email: EmailStr
    password: str

    @classmethod
    def create(cls):
        return cls(username=fake.last_name(),
                   email=fake.ascii_safe_email(),
                   password=str(random.randint(1_000_000, 9_999_999)))


class UserModelUI(Model):
    id: Optional[int] = None
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True
