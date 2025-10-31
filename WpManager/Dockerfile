FROM python:alpine

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev \
    && apk add --no-cache mysql-client\
    && apk add --no-cache docker-compose

RUN mkdir /static
RUN chmod 775 /static

RUN adduser -D worker
RUN chown -R worker:worker /static

#EL GUID DEL GRUPO DE DOCKER TIENE QUE SER IGUAL DEL HOST
RUN addgroup -g 989 docker 
RUN addgroup worker docker

WORKDIR /home/worker
RUN mkdir App
WORKDIR /home/worker/App

COPY --chown=worker:worker ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
    
COPY ./App .

EXPOSE 8000
STOPSIGNAL SIGTERM

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

USER worker