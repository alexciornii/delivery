FROM python:3

LABEL Author="Ciornii Alexandr"
LABEL E-mail="alex.ciornii@gmail.com"
LABEL version="0.1"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PIPENV_VENV_IN_PROJECT 1

RUN mkdir -p /usr/src/app/
COPY Pip* /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --skip-lock

ADD ./prj /usr/src/app/

EXPOSE 8000
EXPOSE 27017

CMD ./manage.py runserver
