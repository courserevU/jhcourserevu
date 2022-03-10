FROM python:3.10.2

ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

# COPY requirements.txt requirements.txt
# COPY ./jhcourserevu/local_settings.py /code/jhcourserevu/local_settings.py
RUN pip3 install -r /code/requirements.txt
