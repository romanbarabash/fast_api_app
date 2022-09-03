import pytest

from backend.models.jobs import JobModelAPI


@pytest.fixture()
def create_job(get_job_service):
    return get_job_service.create_job(JobModelAPI.create())
