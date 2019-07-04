FROM python:3.7-slim

RUN python -m pip install --upgrade pip

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY . .
