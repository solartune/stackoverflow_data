up-dev:
	docker-compose -f docker-compose.yml -p stackoverflow_data-dev up -d

build-dev:
	docker network create infra_default || true
	docker network create stackoverflow_data_network || true
	docker-compose -f docker-compose.yml -p stackoverflow_data-dev build

stop-dev:
	docker-compose -f docker-compose.yml -p stackoverflow_data-dev stop

down-dev:
	docker-compose -f docker-compose.yml stackoverflow_data-dev down

reload-dev:
	docker exec -ti stackoverflowdatadev_app_1 deploy/sh_scripts/reload_gunicorn.sh

logs-dev:
	docker logs --tail=200 stackoverflowdatadev_app_1

restart-dev:
	docker restart stackoverflowdatadev_app_1

shell-dev:
	docker exec -ti stackoverflowdatadev_app_1 ./manage.py shell_plus

tests-dev:
	docker exec -ti stackoverflowdatadev_app_1 ./manage.py test

cmd-dev:
	docker exec -ti stackoverflowdatadev_app_1 $(CMD)

manage-dev:
	docker exec -ti stackoverflowdatadev_app_1 ./manage.py $(CMD)

restart-prod:
	docker restart stackoverflow_dataprod_app_1

logs-prod:
	docker logs --tail=200 stackoverflow_dataprod_app_1

build-prod:
	docker network create infra_default || true
	docker network create stackoverflow_data_network || true
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml -p stackoverflow_data-prod build

shell-prod:
	docker exec -ti stackoverflow_dataprod_app_1 ./manage.py shell_plus

tests-prod:
	docker exec -ti stackoverflow_dataprod_app_1 ./manage.py test

cmd-prod:
	docker exec -ti stackoverflow_dataprod_app_1 $(CMD)

manage-prod:
	docker exec -ti stackoverflow_dataprod_app_1 ./manage.py $(CMD)
