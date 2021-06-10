MANAGE = python blog/manage.py
PROJECT_DIR=$(shell pwd)
WSGI_PORT=8000


run:
	$(MANAGE) runserver 0.0.0.0:$(WSGI_PORT)

make-migrate:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

freeze:
	pip freeze > requirements.txt

rabbit_run:
	systemctl enable rabbitmq-server
	systemctl start rabbitmq-server

rabbit_status:
	systemctl status rabbitmq-server

celery:
	cd blog && celery -A blog worker -l info

celery-beat:
	cd blog && rm -rf celerybeat.pid && celery -A blog beat -l INFO

shell:
	$(MANAGE) shell_plus --print-sql

fill_posts:
	$(MANAGE) fill_posts

start_memcached:
	systemctl start memcached

stop_memcached:
	systemctl stop memcached

restart_memcached:
	systemctl restart memcached

flake:
	flake8 ./blog

createsuperuser:
	$(MANAGE) createsuperuser

gunicorn_run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/blog blog.wsgi --timeout 60 --log-level debug --max-requests 10000

collect_static:
	$(MANAGE) collectstatic

run_nginx:
	systemctl start nginx

stop_nginx:
	systemctl stop nginx

reload_nginx:
	systemctl reload nginx

test_run:
	cd blog && pytest

tst:
	cd blog && pytest --cov=main --cov-report=html --cov-fail-under=40
	xdg-open static_content/coverage/index.html

docker_run:
	docker run --rm -t -d -p 8222:8111 --name my_blog blog:v1

docker_build:
	docker build -t blog:v1 .

docker_stop:
	docker container stop my_blog

dkr-run_dev: dkr-down
	$(eval RUN_COMMAND=run)
	docker-compose up -d --build
	make copy-static

dkr-run_production: dkr-down
	$(eval RUN_COMMAND=gunicorn_run)
	docker-compose up -d --build
	make docker collect-static
	make copy-static

dkr-down:
	docker-compose down

copy-static:
	docker exec -it blog-backend python ./blog/manage.py collectstatic --noinput
	docker cp blog-backend:tmp/static_content/static /tmp/static
#	docker cp /tmp/static nginx:/etc/nginx/static
