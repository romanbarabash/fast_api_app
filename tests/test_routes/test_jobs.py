from backend.models.jobs import JobModelUI


def test_create_job(client, normal_user_token_headers):
    job = JobModelUI.create().to_json()

    response = client.post(url="/job/create-job", data=job, headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["title"] in job

def test_retreive_job_by_id(client, normal_user_token_headers):
    job = JobModelUI.create().to_json()

    client.post(url="/job/create-job", data=job, headers=normal_user_token_headers)
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] in job
