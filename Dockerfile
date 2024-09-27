FROM python:3.12-alpine

WORKDIR /app

COPY ./reqs.txt ./

RUN pip install --no-cache-dir -r reqs.txt

COPY . . 
