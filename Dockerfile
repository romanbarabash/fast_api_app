FROM python:3.9.6-slim

WORKDIR /app
COPY . .

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# start app
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8008"]
