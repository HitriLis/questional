FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /questional
WORKDIR /questional
COPY requirements.txt /questional/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /questional/