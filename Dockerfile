FROM python:3.10-slim-bullseye@sha256:9d1db839c73288a0c3a44000deffaaead48695cb5144daf9ae9f836235291398

USER root

RUN mkdir -p /usr/app

WORKDIR /usr/app

COPY requirements.txt /usr/app/requirements.txt

RUN pip3 install -r /usr/app/requirements.txt

RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

RUN chown python:python /usr/app

COPY . /usr/app

USER python

CMD [ "gunicorn", "--bind" , "0.0.0.0:5000", "--log-level", "debug", "--timeout", "5", "--threads", "2", "app:app"]