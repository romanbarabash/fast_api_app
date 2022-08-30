import uvicorn
from fastapi import FastAPI

from backend.api.base_route import api_router
from backend.config import PROJECT_TITLE, PROJECT_VERSION
from backend.db.__init__ import Base
from backend.db.session import engine


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


@app.get('/')
# TODO - remove
def hello_api():
    return {'detail': 'Hello World'}


if __name__ == '__main__':
    uvicorn.run(app=app, port=8000, debug=True)
