## Django Development With Docker Compose and Machine

Featuring:

- Docker v18.09.2
- Docker Compose v1.23.2
- Docker Machine v0.16.1
- Python 3.7.3
- Postgresql
- MySQL 5.7

Original Blog post -> https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/

Building on the original repo, this repo adds the following capabilities;

1. Is compatible with the original repo and simplifies running the compose stack
1. Adds flexibility by using environment variables to make the service highly configurable
1. Allows switching between postgres or mysql database.
1. Allows the use of an existing database configured by the DB_TYPE=remote & DB_* environment variables
1. Runs migrations before starting django
1. Adds live reload capability for the django code

### General Instructions

1. Start new machine - `docker-machine create -d virtualbox dev`
1. Configure your shell to use the new machine environment - `eval $(docker-machine env dev)`
1. Build and Start services - `docker-compose up -d`
1. Grab IP - `docker-machine ip dev` - and view in your browser

### Advanced Usage
To use existing remote database, change the following in .env;
1. DJANGO_DB_* variables to match your remote database
1. DB_TYPE=remote
1. Run `docker-compose up -d`

To switch databases, change the following in .env;
1. DB_TYPE to mysql, postgres or sqlite
1. If database was already started previously, run `docker-compose stop database && docker-compose rm -f database`
1. Run `docker-compose up -d`

### Troubleshooting
If you encounter this error

```sh
Cannot start service web: driver failed programming external connectivity on endpoint
 failed: port is already allocated
Encountered errors while bringing up the project.
```

* Modify your env file and change the exposed ports on host
* Alternatively, shut down services on the host that are bound to the ports
* Once done run `docker-compose up -d`


