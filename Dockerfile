FROM python:3.9 as builder_python_blog

RUN apt-get update && apt-get install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

FROM builder_python_blog as builder

COPY blog/ blog/
COPY commands/ commands/
RUN chmod +rx -R commands
COPY ./Makefile Makefile


RUN useradd -ms /bin/bash admin
RUN chown -R admin:admin /srv/project
RUN chmod 755 /srv/project
USER admin

# CMD ["python", "./blog/manage.py", "runserver", "0.0.0.0:8111"]

# EXPOSE 8111
