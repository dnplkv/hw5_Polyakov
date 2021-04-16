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