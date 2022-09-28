from typing import List

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.api.routes.base_route import api_router
from backend.db.__init__ import Base
from backend.db.queries.jobs import list_jobs
from backend.db.session import engine, get_db
from backend.models.jobs import JobModelUI
from config import PROJECT_TITLE, PROJECT_VERSION


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start():
    app = FastAPI(title=PROJECT_TITLE, version=PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start()


@app.get('/', tags=['Home'], response_model=List[JobModelUI])
def get_all_jobs(db: Session = Depends(get_db)):
    return list_jobs(db=db)


if __name__ == '__main__':
    uvicorn.run(app=app, port=8008, debug=True)
