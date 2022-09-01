from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.api.api_models.jobs import JobCreateModel, ShowJobModel
from backend.api.routes.route_login import get_user_from_token
from backend.db import User
from backend.db.queries.jobs import create_new_job, retreive_job, list_jobs, update_job_by_id, delete_job_by_id
from backend.db.session import get_db

router = APIRouter()


@router.post("/create-job", response_model=ShowJobModel)
def create_job(job: JobCreateModel, db: Session = Depends(get_db), current_user: User = Depends(get_user_from_token)):
    job = create_new_job(job_model=job, db=db, owner_id=current_user.id)
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


@router.put("/update/{id}")
def update_job(id: int, job: JobCreateModel, db: Session = Depends(get_db), current_user: User = Depends(get_user_from_token)):
    owner_id = current_user.id
    job_retrieved = retreive_job(id=id, db=db)
    if not job_retrieved:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist")
    if job_retrieved.owner_id == current_user.id or current_user.is_superuser:
        update_job_by_id(id=id, job=job, db=db, owner_id=owner_id)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="No permission to perform update operation")
    return {"detail": "Successfully updated data."}


@router.delete("/delete/{id}")
def delete_job(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_user_from_token)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist")
    if job.owner_id == current_user.id or current_user.is_superuser:
        delete_job_by_id(id=id, db=db)
        return {"detail": "Job Successfully deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_401_NOT_FOUND,
                            detail="No permission to perform delete operation")