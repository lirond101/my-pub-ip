FROM python:3.9-slim-bullseye

USER root

RUN mkdir -p /app/my-pub-ip

COPY requirements.txt /app/my-pub-ip/requirements.txt

RUN pip3 install -r /app/my-pub-ip/requirements.txt

COPY . /app/my-pub-ip

WORKDIR /app/my-pub-ip

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
