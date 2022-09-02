from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from requests import Session

from backend.config import TOKEN_EXPIRE_TIME, SECRET_KEY, ALGORITHM
from backend.api.access_token import create_access_token
from backend.db.hashing import Hasher
from backend.db.queries.login import get_user
from backend.db.session import get_db

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


def _authenticate_user(username: str, password: str, db: Session):
    user = get_user(username=username, db=db)
    if not user or not Hasher.verify_password(password, user.hashed_password):
        return None
    return user


def get_user_from_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username=username, db=db)
    if user is None:
        raise credentials_exception
    return user


@router.post("/token")
def login_with_token(form_data: OAuth2PasswordRequestForm = Depends(),
                     db: Session = Depends(get_db)):
    user = _authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")

    access_token_expire = timedelta(minutes=TOKEN_EXPIRE_TIME)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expire)
    # response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)

    return {"access_token": access_token,
            "token_type": "bearer"}