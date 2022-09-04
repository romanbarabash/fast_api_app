from backend.models.jobs import JobModelAPI
from tests.services.base import BaseService


class JobsService(BaseService):

    def __init__(self, client, headers):
        super().__init__(client, headers)

    def create_job(self, job: JobModelAPI):
        path = '/job/create-job'
        return self.client.post(url=path, data=job.to_json(), headers=self.headers)

    def get_job_by_id(self, id: int):
        path = f'/job/get/{id}'
        return self.client.get(url=path)

    def get_all_jobs(self):
        path = '/job/all'
        return self.client.get(url=path)
