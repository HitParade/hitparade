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

## Additional Web service steps

To build assets, from the `web/hitparade` directory, run

 ```bash
npm install
npm run build
```

## Additional steps to load base data

Load teams, players & BIS Data
```bash
docker-compose exec web ./manage.py load-teams
docker-compose exec web ./manage.py load-players
docker-compose exec web ./manage.py load-games
docker-compose exec web ./manage.py load-bis-historical
docker-compose exec web ./manage.py load-bis-daily --date 20160505
```

Run tests
```bash
docker-compose exec web py.test -s
```
