import pytest

from backend.models.jobs import JobModelAPI
from tests.services.base import AssertResponse
from tests.services.json_schemas.job_schemas import job_schema, all_jobs_schema


@pytest.mark.positive
def test_create_job(get_job_service):
    job_service = get_job_service
    job = JobModelAPI.create()

    response = job_service \
        .create_job(job=job)

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(7) \
        .value_equals(actual_response_item="title", expected_text=job.title) \
        .validate_schema(job_schema)


@pytest.mark.negative
def test_create_job_empty_body(get_job_service):
    job_service = get_job_service

    response = job_service \
        .create_job(job=None)

    AssertResponse(response) \
        .status_code_is(422) \
        .value_equals(actual_response_item="detail", expected_text='value_error.missing', is_contains=True)



@pytest.mark.positive
def test_retreive_job_by_id(get_job_service, create_job):
    job_service = get_job_service
    job = create_job.json()
    response = job_service.get_job_by_id(id=job.get('id'))

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(7) \
        .value_equals(actual_response_item="title", expected_text='') \
        .validate_schema(job_schema)



@pytest.mark.negative
def test_retreive_job_incorrect_id(get_job_service):
    job_service = get_job_service
    incorrect_id = 0
    response = job_service.get_job_by_id(id=incorrect_id)

    AssertResponse(response) \
        .status_code_is(404) \
        .value_equals(actual_response_item="detail", expected_text=f'Job with id {incorrect_id} does not exist.')



@pytest.mark.positive
def test_retreive_all_jobs(get_job_service, create_job):
    job_service = get_job_service
    response = job_service.get_all_jobs()

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(1) \
        .validate_schema(all_jobs_schema)



@pytest.mark.positive
def test_update_job(get_job_service, create_job):
    job_service = get_job_service
    current_job = create_job.json()
    updated_job = JobModelAPI.create()

    response = job_service \
        .update_job(id=current_job.get('id'), job=updated_job)

    AssertResponse(response) \
        .status_code_is(200) \
        .value_equals(actual_response_item='detail', expected_text='Job Successfully updated.')

    response = job_service \
        .get_job_by_id(id=current_job.get('id'))

    AssertResponse(response) \
        .status_code_is(200) \
        .has_items(7) \
        .validate_schema(job_schema) \
        .value_equals(actual_response_item="title", expected_text=updated_job.title)



@pytest.mark.negative
def test_update_job_incorrect_id(get_job_service, create_job):
    job_service = get_job_service
    updated_job = JobModelAPI.create()
    incorrect_id = 0

    response = job_service \
        .update_job(id=incorrect_id, job=updated_job)

    AssertResponse(response) \
        .status_code_is(404) \
        .value_equals(actual_response_item="detail", expected_text=f'Job with id {incorrect_id} does not exist.')



@pytest.mark.positive
def test_delete_job(get_job_service, create_job):
    job_service = get_job_service
    job = create_job.json()

    response = job_service \
        .delete_job(id=job.get('id'))

    AssertResponse(response) \
        .status_code_is(200) \
        .value_equals(actual_response_item='detail', expected_text='Job Successfully deleted.')

    response = job_service \
        .get_job_by_id(id=job.get('id'))

    AssertResponse(response) \
        .status_code_is(404)


@pytest.mark.negative
def test_delete_job_incorrect_id(get_job_service, create_job):
    job_service = get_job_service
    incorrect_id = 0

    response = job_service \
        .delete_job(id=incorrect_id)

    AssertResponse(response) \
        .status_code_is(404) \
        .value_equals(actual_response_item="detail", expected_text=f'Job with id {incorrect_id} does not exist.')
