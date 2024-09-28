FROM python:3.12-alpine

RUN apt-get update
RUN apt-get install vim

WORKDIR /app

COPY ./reqs.txt ./

RUN pip install --no-cache-dir -r reqs.txt

COPY . . 
