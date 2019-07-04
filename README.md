## Django Development With Docker Compose and Machine

Featuring:

- Docker v18.09.2
- Docker Compose v1.23.2
- Docker Machine v0.16.1
- Python 3.7.3
- MySQL 5.7

Original Blog post -> https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/

Building on the original repo, this repo adds the following capabilities;

1. Uses MySQL instead of Postgresql
1. Runs migrations before starting django
1. Allows the use of an existing mysql db configured by the DB_* environment variables
1. Adds live reload capabaility for the source code

### General Instructions

1. Start new machine - `docker-machine create -d virtualbox dev`
1. Configure your shell to use the new machine environment - `eval $(docker-machine env dev)`
1. Build and Start services - `docker-compose up -d`
1. Grab IP - `docker-machine ip dev` - and view in your browser

If you encounter this error

```sh
Cannot start service web: driver failed programming external connectivity on endpoint
 failed: port is already allocated
Encountered errors while bringing up the project.
```

* Modify your env file and change the exposed ports on host
* Alternatively, shut down services on the host that are bound to the ports

