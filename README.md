## To run app:

### With Docker:
1. run `docker-compose up --build` to create images and up containers

- The app will be available under `0.0.0.0:8008/`
- Docs will be available `0.0.0.0:8008/docs`

### Locally:

Before run locally, setup db:
- postgresql should be installed
- postgres server should be started with correct settings
- create `.env` file based on `env.example` file
- under `.env`  use DATABASE_URL for local connections


To run locally:
1. creating a virtual environment `python -m venv venv`
2. activating a virtual environment `source venv/bin/activate` - Linux or macOS,
`.\venv\Scripts\activate` - Windows
3. installing packages `pip install -r requirements.txt`
4. run `backend/app.py` as is OR run `uvicorn backend.app:app --reload` as command in the terminal

- The app will be available under `127.0.0.1:8000/`
- Docs will be available `127.0.0.1:8000/docs`

## To run tests:

### With Docker:

TO DO

### To run locally:

run `pytest /tests`

