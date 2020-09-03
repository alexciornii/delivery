FROM python:3

LABEL Author="Ciornii Alexandr"
LABEL E-mail="alex.ciornii@gmail.com"
LABEL version="0.1"

ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install 'pipenv==2018.11.26' && \
    pipenv install --ignore-pipfile

ADD . /app

EXPOSE 5000

CMD ./bin/run
