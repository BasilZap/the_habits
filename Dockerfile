
FROM python:3.11

WORKDIR /course_project

COPY ./requirements.txt /course_project/

RUN pip install -r /course_project/requirements.txt

COPY . .