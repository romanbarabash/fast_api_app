import pytest

from backend.models.jobs import JobModelAPI
from backend.models.users import UserModelAPI


@pytest.fixture
def create_job(get_job_service):
    return get_job_service.create_job(JobModelAPI.create())

@pytest.fixture
def create_user(get_user_service):
    user_model = UserModelAPI.create()
    return get_user_service.create_user(user=user_model)
