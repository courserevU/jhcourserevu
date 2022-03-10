FROM python:3.9.10

RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip3 install -r /code/requirements.txt

COPY . .
