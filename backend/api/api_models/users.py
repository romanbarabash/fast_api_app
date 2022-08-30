from pydantic import BaseModel, EmailStr


class UserCreateModel(BaseModel):
    username: str
    email: EmailStr
    password: str


class ShowUserModel(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True
