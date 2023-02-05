# syntax=docker/dockerfile:1

FROM python:latest

ADD . /app
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD [ "python", "main.py"]