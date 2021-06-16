FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /questionnaire_app
WORKDIR /questionnaire_app
COPY requirements.txt /questionnaire_app/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /questionnaire_app/