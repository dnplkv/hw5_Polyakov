FROM python:3.9

RUN apt-get update && apt-get install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project
COPY requirements.txt /tmp/requirements.txt
COPY blog/ blog/

RUN pip install -r /tmp/requirements.txt
CMD ["python", "./blog/manage.py", "runserver", "0.0.0.0:8111"]

# EXPOSE 8111
