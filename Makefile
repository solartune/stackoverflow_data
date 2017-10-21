up-dev:
	docker-compose -f docker-compose.yml -p avanan-dev up -d

build-dev:
	docker network create infra_default || true
	docker network create avanan_network || true
	docker-compose -f docker-compose.yml -p avanan-dev build

stop-dev:
	docker-compose -f docker-compose.yml -p avanan-dev stop

down-dev:
	docker-compose -f docker-compose.yml avanan-dev down

reload-dev:
	docker exec -ti avanandev_app_1 deploy/sh_scripts/reload_gunicorn.sh

logs-dev:
	docker logs --tail=200 avanandev_app_1

restart-dev:
	docker restart avanandev_app_1

shell-dev:
	docker exec -ti avanandev_app_1 ./manage.py shell_plus

tests-dev:
	docker exec -ti avanandev_app_1 ./manage.py test

cmd-dev:
	docker exec -ti avanandev_app_1 $(CMD)

manage-dev:
	docker exec -ti avanandev_app_1 ./manage.py $(CMD)

restart-prod:
	docker restart avananprod_app_1

logs-prod:
	docker logs --tail=200 avananprod_app_1

build-prod:
	docker network create infra_default || true
	docker network create avanan_network || true
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml -p avanan-prod build

shell-prod:
	docker exec -ti avananprod_app_1 ./manage.py shell_plus

tests-prod:
	docker exec -ti avananprod_app_1 ./manage.py test

cmd-prod:
	docker exec -ti avananprod_app_1 $(CMD)

manage-prod:
	docker exec -ti avananprod_app_1 ./manage.py $(CMD)
