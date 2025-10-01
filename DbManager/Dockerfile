FROM python:alpine

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev \
    && apk add --no-cache mysql-client

WORKDIR /App

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt && \ 
    adduser \                                           
        --disabled-password \
        --no-create-home \
        django-user

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

USER django-user