FROM tiangolo/uwsgi-nginx-flask:flask

RUN apt-get update && \
  apt-get install -y zip && \
  rm -rf /var/lib/apt/lists/*

COPY ./app /app

RUN pip install -r /app/requirements.txt

EXPOSE 80 81
