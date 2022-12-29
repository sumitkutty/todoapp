#FROM python:3.8
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
FROM ubuntu:trusty
FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev python3-pip 


WORKDIR /app

COPY . .


RUN pip3 install --upgrade pip && pip install -r /app/requirements.txt


RUN ["python3", "database.py","-d", "DB/todos.db"]


EXPOSE 8080

CMD ["python3", "main.py"]

