from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.models.users import UserModelUI, UserModelAPI
from backend.db.queries.users import create_new_user
from backend.db.session import get_db


router = APIRouter()


@router.post("/", response_model=UserModelUI)
def create_user(user: UserModelAPI, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user
