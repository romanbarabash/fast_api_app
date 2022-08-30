from sqlalchemy.orm import Session

from backend.api.api_models.jobs import JobCreateModel
from backend.db import Job



def create_new_job(job_model: JobCreateModel, db: Session, owner_id: int):
    job = Job(title=job_model.title,
                    company=job_model.company,
                    location=job_model.location,
                    description=job_model.description,
                    company_url=job_model.company_url,
                    date_posted=job_model.date_posted,
                    owner_id=owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def retreive_job(id: int, db: Session):
    job = db.query(Job).filter(Job.id == id).first()
    return job


def list_jobs(db: Session):
    jobs = db.query(Job).filter(Job.is_active == True).all()
    return jobs
