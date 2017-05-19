#!/bin/bash

set -e

# write the env to disk for cron jobs
env > /root/.env
sed -i 's/^/export /' /root/.env

until mysql -h "$MYSQL_HOST" -u "$MYSQL_SA_USER" -p$MYSQL_PASSWORD -e ";"; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"

cd /code/

python manage.py migrate --fake-initial

echo $TIER

if [[ -n $TIER ]]
then
  if [ "$TIER" == "dev" ]
  then
    echo "Fixturizing"
    python manage.py loaddata fixtures/accounts.json
  elif [ "$TIER" == "stage" ] || [ "$TIER" == "prod" ]
  then
    echo "We're in $TIER, not Fixturizing"
  fi
else
  echo -e "TIER not set\n"
  exit
fi

echo "Starting nginx."
service nginx start

echo "Starting UWSGI (http)."
uwsgi --ini /etc/uwsgi/hitparade-uwsgi.ini
