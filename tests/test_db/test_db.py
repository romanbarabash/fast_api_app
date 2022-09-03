from sqlalchemy.orm import Session

from backend.db.queries.jobs import create_new_job, retreive_job
from backend.models.jobs import JobModelUI
from backend.utils import create_random_owner


def test_retreive_job_by_id(db_session: Session):
    job_model = JobModelUI.create()
    owner = create_random_owner(db=db_session)
    job = create_new_job(job_model=job_model, db=db_session, owner_id=owner.id)
    retreived_job = retreive_job(id=job.id, db=db_session)

    assert retreived_job.id == job.id
    assert retreived_job.title == job_model.title
