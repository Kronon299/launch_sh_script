b: docker-compose.yaml
	docker-compose build

s: docker-compose.yaml
	docker-compose up pg
	sleep 3
	docker-compose up web

ba:
	docker-compose exec web bash

i: s m cs du

l:
	docker-compose logs -f

r:
	docker-compose restart

stop:
	docker-compose stop

d:
	docker-compose down --volumes
