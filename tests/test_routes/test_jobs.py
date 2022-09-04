import pytest

from backend.models.jobs import JobModelAPI
from tests.services.base import AssertResponse
from tests.services.json_schemas.job_schemas import job_schema, all_jobs_schema


#@pytest.mark.skip()
def test_create_job(get_job_service):
    job_service = get_job_service
    job = JobModelAPI.create()

    response = job_service \
        .create_job(job=job)

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(7) \
        .value_matcher(actual_response_item="title", expected_item=job.title) \
        .validate_schema(job_schema)


#@pytest.mark.skip()
def test_retreive_job_by_id(get_job_service, create_job):
    job_service = get_job_service
    job = create_job.json()
    response = job_service.get_job_by_id(id=job.get('id'))

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(7) \
        .value_matcher(actual_response_item="title", expected_item=job.get('title')) \
        .validate_schema(job_schema)


def test_retreive_all_jobs(get_job_service, create_job):
    job_service = get_job_service
    response = job_service.get_all_jobs()

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(1) \
        # .validate_schema(all_jobs_schema) #TODO
