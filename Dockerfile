FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
  apt-get install -y mysql-client nginx vim && \
  rm -rf /var/lib/apt/lists/* && \
  rm /etc/nginx/sites-available/default

RUN mkdir -p /code/requirements && mkdir -p /etc/uwsgi/
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt

ADD hitparade/ /code/
ADD docker/entrypoint.sh /code/
ADD docker/hitparade-nginx.conf /etc/nginx/sites-enabled/
ADD docker/hitparade-uwsgi-params /etc/nginx/
ADD docker/hitparade-uwsgi.ini /etc/uwsgi/

EXPOSE 80

CMD ["/code/entrypoint.sh"]
