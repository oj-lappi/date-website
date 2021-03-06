FROM python:3.6-slim
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install gcc libldap2-dev libsasl2-dev libssl-dev git && \
    rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
WORKDIR /
RUN git clone https://github.com/oj-lappi/date-overlay.git
RUN cp -r date-overlay/* /code
WORKDIR /code
