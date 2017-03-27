FROM tiangolo/uwsgi-nginx-flask:flask

COPY ./app /app

RUN pip install -r /app/requirements.txt

EXPOSE 80 81
