# Blog

Personal notices and reminds about this "blog" project for studying purposes.

## Running gunicorn and collect static

Use this command to run gunicorn of this project.

Notice: Currently specified port is :8081. You can change it on other in Makefile, 
as well as name of command for visibility.

```bash
make gunicorn_run_8081:
```

To create static folder dir for its future use enter next command:
```bash
make collect_static
```

## Nginx configuration (/etc/nginx/nginx.conf)

```
events {}
http {
	include /etc/nginx/mime.types;
	sendfile on;
	server {
		listen 80;
		listen [::]:80;
		server_name 127.0.0.1 blog.com;

		location /static/ {
			root /home/danny/Hillel_Advanced/hw5_Polyakov/static_content;
		}

		location / {
			proxy_pass http://127.0.0.1:8081;
		}
	}
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## TravisCI
[![Build Status](https://travis-ci.com/dnplkv/hw5_Polyakov.svg?branch=lint_br)](https://travis-ci.com/dnplkv/hw5_Polyakov)