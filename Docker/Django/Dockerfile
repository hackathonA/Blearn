FROM python:3.10.5-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -U pip && \
    pip install -r requirements.txt

COPY Django_App/ /code/
