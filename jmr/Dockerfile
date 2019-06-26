# pull official base image
FROM python:3.6-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy project
COPY . /usr/src/app

# run server
CMD gunicorn recruitment.wsgi --bind 0.0.0.0:8000
