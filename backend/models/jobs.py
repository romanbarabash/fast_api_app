from datetime import date, datetime
from typing import Optional

from backend.models.base import Model, fake


class JobModel(Model):
    title: str
    company: str
    location: str
    description: str
    company_url: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()

    @classmethod
    def create(cls):
        return cls(title=fake.word().title() + ' Developer',
                   company=fake.word().title() + ' Solutions',
                   company_url=f'www.{fake.word()}-solutions.com',
                   location='US, CA',
                   description=f'What drives us: {fake.word()} and {fake.word()}',
                   date_posted=str(datetime.now().date()))


class JobModelAPI(JobModel):
    owner_id: Optional[str] = None


class JobModelUI(JobModel):
    class Config():
        orm_mode = True
