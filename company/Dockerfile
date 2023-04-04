FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/company
ADD . .

RUN apk add --update --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers tree vim bash

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt