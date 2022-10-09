## To run app and tests:

### With Docker:
1. run `docker-compose up --build` to create images and up db, adminer, app, tests containers

- The app will be available under `0.0.0.0:8008/`
- Docs will be available `0.0.0.0:8008/docs`
- Tests will run and generate report into `report.html`

To open tests report:

1. run
`docker cp fast_api_app_tests_1:/app/report.html report.html` to copy report from container to local machine 
2. run `open report.html` to open report 


### Locally:

Before run locally, setup db:
- postgresql should be installed
- postgres server should be started with correct settings
- create `.env` file based on `env.example` file
- under `.env`  use DATABASE_URL for local connections


Run app locally:
1. creating a virtual environment `python -m venv venv`
2. activating a virtual environment `source venv/bin/activate` - Linux or macOS,
`.\venv\Scripts\activate` - Windows
3. installing packages `pip install -r requirements.txt`
4. run `backend/app.py` as is OR run `uvicorn backend.app:app --reload` as command in the terminal:
- The app will be available under `127.0.0.1:8000/`
- Docs will be available `127.0.0.1:8000/docs`


Run tests and open tests report:
1. run `pytest --html=report.html tests` 
2. open `report.html` file

