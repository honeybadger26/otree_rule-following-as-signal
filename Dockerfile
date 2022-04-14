FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8000
CMD sh -c 'echo oTree app is running && otree devserver 0.0.0.0:8000'
