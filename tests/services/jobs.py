from backend.models.jobs import JobModelAPI


class JobsService:

    def __init__(self, client, headers):
        self.client = client
        self.headers = headers

    def create_job(self, job: JobModelAPI):
        path = '/job/create-job'
        return self.client.post(url=path, data=job.to_json(), headers=self.headers)

    def get_job_by_id(self, id: int):
        path = f'/job/get/{id}'
        return self.client.get(url=path)
