from sqlalchemy.orm import Session

from backend.db import Job
from backend.schemas.jobs import JobCreate


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job_model = Job(title=job.title,
                    company=job.company,
                    location=job.location,
                    description=job.description,
                    company_url=job.company_url,
                    date_posted=job.date_posted,
                    owner_id=owner_id)
    db.add(job_model)
    db.commit()
    db.refresh(job_model)
    return job_model


def retreive_job(id: int, db: Session):
    job = db.query(Job).filter(Job.id == id).first()
    return job


def list_jobs(db: Session):
    jobs = db.query(Job).filter(Job.is_active == True).all()
    return jobs
