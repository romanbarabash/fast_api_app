from pydantic import BaseModel, EmailStr


class UserModelAPI(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserModelUI(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True
