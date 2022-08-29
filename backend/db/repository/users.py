from sqlalchemy.orm import Session

from backend.core.hashing import Hasher
from backend.db.models.users import User
from backend.schemas.users import UserCreate


def create_new_user(user: UserCreate, db: Session):
    user_model = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False)
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model
