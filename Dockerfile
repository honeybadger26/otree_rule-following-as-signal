FROM python:3.9

WORKDIR /usr/src/app

COPY requirements*.txt .
RUN pip install -r requirements.txt

CMD sh -c 'otree prodserver 0.0.0.0:8000'