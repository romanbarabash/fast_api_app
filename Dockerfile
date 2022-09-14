FROM python:3.7-alpine
WORKDIR .
COPY . .

RUN apk add postgresql-libs
RUN apk add --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN pip install -e .
RUN apk --purge del .build-deps

CMD ["uvicorn", "uvicorn backend.app:app", "--host", "0.0.0.0", "--port", "80"]