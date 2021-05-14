run:
	python blog/manage.py runserver 0.0.0.0:8000

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

createsuperuser:
	python blog/manage.py createsuperuser

gunicorn_run_8081:
	gunicorn -w 4 -b 0.0.0.0:8081 --chdir /home/danny/Hillel_Advanced/hw5_Polyakov/blog blog.wsgi --timeout 60 --log-level debug --max-requests 10000

collect_static:
	python blog/manage.py collectstatic

run_nginx:
	systemctl start nginx

stop_nginx:
	systemctl stop nginx

reload_nginx:
	systemctl reload nginx
