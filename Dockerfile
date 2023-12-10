FROM ubuntu:16.04

FROM python:3.8-slim

# Rest of your Dockerfile

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3-pip python-dev-is-python3


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD python /app/model.py && python /app/server.py


 
