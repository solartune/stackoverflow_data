# Stackoverflow data

## About

This is just a simple demo project for work with Stackoverflow API. You can make request for a list of posts by user ID or 
get all of your posts via OAuth.

## Technical details
Python=3.6.2 </br>
Django=1.11.6 </br>
I use there SQLite database since I don't see any reasons for use another one like Postgres in this project. However you can use it if you want. </br>
For OAuth I use [Python Social Auth library](https://python-social-auth.readthedocs.io/en/latest/index.html).</br>
You can change env variables [there](https://github.com/solartune/stackoverflow_data/blob/master/variables-dev.env).</br>
For production environment you should copy this file, change values and rename the file to `variables-prod.env`.

## Change OAuth data
For development I use test credentials and unfortunately this user has no posts. So you may need to change this data.
As I said before you need to do that in the files of environment variables.

Assotiations according this [documentation](https://python-social-auth.readthedocs.io/en/latest/backends/stackoverflow.html):
- `SOCIAL_AUTH_STACKOVERFLOW_KEY` - client ID
- `SOCIAL_AUTH_STACKOVERFLOW_SECRET` - client secret
- `SOCIAL_AUTH_STACKOVERFLOW_API_KEY` - API key

## How to run

With Docker power and make it can be very easy. </br>
For dev containers:

- `make build-dev`
- `make`
- `make manage-dev CMD=migrate`

Or for production containers:
- `make build-prod`
- `make up-pord`

That's all!
If you can't use make see commands [there](https://github.com/solartune/stackoverflow_data/blob/master/Makefile)

## Useful commands

Below you can see some useful commands for manipulate docker containers via make:

- `make build-dev` - Create networks if they don't exist and build dev images
- `make up-dev` - Run dev containers (shortcut `make`)
- `make stop-dev` - Stop dev containers
- `make down-dev` - Stop containers and remove containers, networks, volumes, and images
- `make restart-dev` - Restart the application container
- `make logs-dev` - Show last 200 logs from the application container
- `make tests-dev` - Run tests
- `make manage-dev CMD='command'` - Run any command realted with manage. E.g.: `make manage-dev CMD=migrate` will do `./manage.py migrate` in the application container
- `make cmd-dev CMD='command'` - Run any command. E.g.: `make cmd-dev CMD=ls` will do `ls` in the application container
- `make reload-prod` - Reload gunicorn in the application container (Only for production)

You can use almost of all commands for manage production containers, just use `prod` insted `dev`. E.g. `make build-prod`.

## If you can't use Docker

In this case you should use standard Django commands. </br>
You should have [virtualenv](https://virtualenv.pypa.io/en/stable/) </br>
I assume that you are in a directory of the project:
- `virtualenv env` - create new virtual environment
- `source env/bin/activate` - activate it
- `pip install -r requirements` - install all requirements to the environment
- `./manage.py migrate` - migrate all rpoject migrations
- `./manage.py runserver` - run dev server
