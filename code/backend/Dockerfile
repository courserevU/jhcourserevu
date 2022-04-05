FROM python:3.10.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy project
COPY . /code/

# Install postgres CLI, helpful if you need to access psql db directly
RUN apt-get update
RUN apt-get -y install postgresql

# Install dependencies
RUN pip install -r requirements.txt
