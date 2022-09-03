from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.models.jobs import JobModelAPI, JobModelUI
from backend.api.routes.login import get_user_from_token
from backend.db import User
from backend.db.queries.jobs import create_new_job, retreive_job, list_jobs, update_job_by_id, delete_job_by_id
from backend.db.session import get_db

router = APIRouter()


@router.post("/create-job", response_model=JobModelUI)
def create_job(job: JobModelAPI, db: Session = Depends(get_db), current_user: User = Depends(get_user_from_token)):
    return create_new_job(job_model=job, db=db, owner_id=current_user.id)


@router.get("/get/{id}", response_model=JobModelUI)
def retreive_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist.")
    return job


@router.get("/all", response_model=List[JobModelUI])
def retreive_all_jobs(db: Session = Depends(get_db)):
    return list_jobs(db=db)


@router.put("/update/{id}")
def update_job(id: int, job: JobModelAPI, db: Session = Depends(get_db), current_user: User = Depends(get_user_from_token)):
    job_retrieved = retreive_job(id=id, db=db)
    if not job_retrieved:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist.")
    if job_retrieved.owner_id == current_user.id or current_user.is_superuser:
        update_job_by_id(id=id, job=job, db=db, owner_id=current_user.id)
        return {"detail": "Job Successfully updated."}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="No permission to perform update operation.")


@router.delete("/delete/{id}")
def delete_job(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_user_from_token)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist")
    if job.owner_id == current_user.id or current_user.is_superuser:
        delete_job_by_id(id=id, db=db)
        return {"detail": "Job Successfully deleted."}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="No permission to perform delete operation.")
