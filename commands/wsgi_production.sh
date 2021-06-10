#!/bin/bash

gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/blog blog.wsgi --timeout 60 --log-level debug --max-requests 10000
