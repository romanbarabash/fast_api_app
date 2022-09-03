from sqlalchemy.orm import Session

from backend.models.jobs import JobModelAPI
from backend.db import Job


def create_new_job(job_model: JobModelAPI, db: Session, owner_id: int):
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


def update_job_by_id(id: int, job: JobModelAPI, db: Session, owner_id: int):
    existing_job = db.query(Job).filter(Job.id == id)
    job.owner_id = owner_id
    if not existing_job.first():
        return False
    existing_job.update(job.__dict__)
    db.commit()
    return True


def delete_job_by_id(id: int, db: Session):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return False
    existing_job.delete(synchronize_session=False)
    db.commit()
    return True
