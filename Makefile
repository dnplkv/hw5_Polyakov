run:
	python blog/manage.py runserver

make-migrate:
	python blog/manage.py makemigrations

migrate:
	python blog/manage.py migrate

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
	python blog/manage.py shell_plus --print-sql

fill_posts:
	python blog/manage.py fill_posts

start_memcached:
	systemctl start memcached

stop_memcached:
	systemctl stop memcached

restart_memcached:
	systemctl restart memcached

flake:
	flake8 ./blog

