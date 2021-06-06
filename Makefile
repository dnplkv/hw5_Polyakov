MANAGE = python blog/manage.py
PROJECT_DIR=$(shell pwd)


run:
	$(MANAGE) runserver 0.0.0.0:8000

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
	celery -A blog worker -l info

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

gunicorn_run_8081:
	gunicorn -w 4 -b 0.0.0.0:8081 --chdir /home/danny/Hillel_Advanced/hw5_Polyakov/blog blog.wsgi --timeout 60 --log-level debug --max-requests 10000

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

