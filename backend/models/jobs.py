import json
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

from backend.utils import fake


class JobModel(BaseModel):
    def to_dict(self):
        return dict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, default=lambda x: str(x))


class JobModelAPI(JobModel):
    title: str
    company: str
    location: str
    description: str
    company_url: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()
    owner_id: Optional[str] = None


class JobModelUI(JobModel):
    title: str
    company: str
    location: str
    company_url: Optional[str]
    date_posted: Optional[date]
    description: Optional[str]

    class Config():
        orm_mode = True

    @classmethod
    def create(cls):
        return cls(title=fake.word().title() + ' Developer',
                   company=fake.word().title() + ' Solutions',
                   company_url=f'www.{fake.word()}-solutions.com',
                   location='US, CA',
                   description=f'What drives us: {fake.word()} and {fake.word()}',
                   date_posted=str(datetime.now().date()))
