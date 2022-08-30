from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.api.api_models.users import ShowUserModel, UserCreateModel
from backend.db.repository.users import create_new_user
from backend.db.session import get_db


router = APIRouter()


@router.post("/", response_model=ShowUserModel)
def create_user(user: UserCreateModel, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user
