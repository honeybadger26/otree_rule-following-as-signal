FROM python:3.9

WORKDIR /usr/src/app

COPY . .
RUN pip install -r requirements.txt && \
    pip uninstall -y uvicorn && \
    pip install uvicorn[standard]

ENV OTREE_PRODUCTION 1
EXPOSE 8000
CMD sh -c 'otree prodserver 0.0.0.0:8000'
