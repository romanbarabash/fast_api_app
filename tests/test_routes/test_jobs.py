import jsonschema

from backend.models.jobs import JobModelAPI
from tests.services.json_schemas.job_schemas import job_schema


def test_create_job(get_job_service):
    job_service = get_job_service
    job = JobModelAPI.create()
    response = job_service.create_job(job=job)

    assert response.status_code == 200
    assert response.json()["title"] == job.title
    jsonschema.validate(response.json(), job_schema)


def test_retreive_job_by_id(get_job_service, create_job):
    job_service = get_job_service
    job = create_job.json()
    response = job_service.get_job_by_id(id=job.get('id'))

    assert response.status_code == 200
    assert response.json()["title"] == job.get('title')
    jsonschema.validate(response.json(), job_schema)
