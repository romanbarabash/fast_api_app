from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class JobModelAPI(BaseModel):
    title: str
    company: str
    location: str
    description: str
    company_url: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()
    owner_id: Optional[str] = None


class JobModelUI(BaseModel):
    title: str
    company: str
    location: str
    company_url: Optional[str]
    date_posted: Optional[date]
    description: Optional[str]

    class Config():
        orm_mode = True
