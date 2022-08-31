from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.api.api_models.jobs import JobCreateModel, ShowJobModel
from backend.db.queries.jobs import create_new_job, retreive_job, list_jobs
from backend.db.session import get_db


router = APIRouter()


@router.post("/create-job", response_model=ShowJobModel)
def create_job(job: JobCreateModel, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job_model=job, db=db, owner_id=owner_id)
    return job


@router.get("/get/{id}", response_model=ShowJobModel)
def retreive_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist")
    return job


@router.get("/all", response_model=List[ShowJobModel])
def retreive_all_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs
