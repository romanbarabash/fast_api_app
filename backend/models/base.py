import json

from faker import Faker
from pydantic import BaseModel

fake = Faker(['en-US'])


class Model(BaseModel):
    def to_dict(self):
        return dict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, default=lambda x: str(x))
