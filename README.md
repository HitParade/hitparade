# Hit Parade

This repo contains all the services to run HitParade.

## Getting Started

The recommended way to install and run this repo is using Docker.

The simplest way to install Docker is to install [the Platform from the official website](https://www.docker.com/products/docker).
The official website offers [a good tutorial](https://docs.docker.com/engine/getstarted/).

For each service, you'll need to create a .env file. The required fields are
listed in .env.skel. The defaults are likely good enough for running an instance
of each service locally.

From the root of the repo;

```bash
$ cp web/.env.skel web/.env
$ docker-compose up -d
```

The app will be available at either [http://localhost/](localhost) or [http://127.0.0.1](127.0.0.1), depending on your setup.

## Additional steps to load base data

Load teams, players & BIS Data
```bash
docker-compose exec web ./manage.py load-teams
docker-compose exec web ./manage.py load-players
docker-compose exec web ./manage.py load-games
docker-compose exec web ./manage.py load-bis-historical
docker-compose exec web ./manage.py load-bis-daily --date 20170301
docker-compose exec web ./manage.py load-atbats
```

## Run tests
```bash
docker-compose exec web ./test.sh
```

## Installing new Python modules
```bash
docker-compose exec web pip install {package}
docker-compose exec web pip freeze > requirements.txt
```

After installing, the stattlepy line needs to be edited back to the github
install. This is because stattlepy currently doesn't have the package available
via PyPi. We've asked Stattleship to do this.

## Admin section

The admin section is available at [http://localhost/admin](http://localhost/admin).

The username / password is; `info@hitparade.co / password`

## Debugging

Things go wrong. Often. Here's a few tips on how to determine what may be happening.

First, check that all the containers are running. Use [docker-compose's ps command](https://docs.docker.com/compose/reference/ps/)to check that all containers are up and running. Here's example output;

```
± |moar-readme ✗| → dco ps
               Name                                 Command                                State                                 Ports
-----------------------------------------------------------------------------------------------------------------------------------------------------
hitparade_rabbit_1                    docker-entrypoint.sh rabbi ...        Up                                    15671/tcp,
                                                                                                                  0.0.0.0:15672->15672/tcp,
                                                                                                                  25672/tcp, 4369/tcp, 5671/tcp,
                                                                                                                  0.0.0.0:5672->5672/tcp
hitparade_redis_1                     /entrypoint.sh redis-server           Up                                    6379/tcp
hitparade_web-db_1                    docker-entrypoint.sh mysqld           Up                                    0.0.0.0:3306->3306/tcp
hitparade_web-js_1                    /usr/local/bin/npm run watch          Up
hitparade_web-worker_1                /usr/local/bin/python /cod ...        Up
hitparade_web_1                       /code/entrypoint-web.sh               Up                                    0.0.0.0:80->80/tcp
```

Should any of the containers show a state of something other than `Up`, the next step is look at the logs for clues. You can use the [docker-compose logs command](https://docs.docker.com/compose/reference/logs/). For example, if the web container, is not up, you can run this command to get the last logs it wrote;

```bash
docker-compose logs web
```

## Common problems

After large PRs are merged, they may contain changes to the code or dependencies that require a rebuild. If a python container contains an error along the lines of `ImportError: No module named celery`, it's most likely because the container needs to be rebuilt. Should that not solve the issue, googling the module and installing may solve. Looking through closed PRs may also shed some light on the issue.

Occasionally, when your computer is shutdown, the docker VM may experience clock lag. This will cause certain time-sensitive operations to error. For example, calls to the AWS API are dependent on the issuing machine's clock being correct. To rememdy this, you need to restart the Docker service, which can be done from the tray icon.

## Shell'ing into containers

Sometimes it's easier to debug an issue from inside the container. The issue may not be getting logged properly or you may need to run additional commands to experiment. To get a shell into a container, use the [docker-compose exec command](https://docs.docker.com/compose/reference/exec/) with shell executable for the container. (The vast majority of your containers have bash shell. To figure out which shell you should be passing, you'll have to trace the container heritage.) For example;

```bash
docker-compose exec web /bin/bash
```
