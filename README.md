# Blog

Personal notices and reminds about this "blog" project for studying purposes. This repository presents a website with a blog functionality in core purpose. Work on this repository has been started during Python Advanced course in Hillel IT School. Any suggestions and advices on this repository are highly appreciated! 😉

## Following tools and technlogies were used in this project:
| Back       			| Front         | Additional tools |
| -------------  		|-------------	| -----	|
| Python   	 		| HTML5 	| Docker, Docker-compose |
| Django      	 		| CSS3 		| GIT |
| Nginx 			| Vue.js 	| Bash |
| wsgi(gunicorn/uwsgi)  	| jQuery     	| Makefile |
| Celery, Redis, Memcached	| Bootstrap     | SQLite3, PostgreSQL |


## Install requirements

```bash
$ pip install -r requirements.txt
```
## To start project locally:

```bash
$ make run
```

## To start project in Docker:

In development mode:

```bash
$ make dkr-run_dev
```

In produciton mode:

```bash
$ make dkr-run_production
```

## Some screenshots of project:
<kbd><img src="![Screenshot from 2021-07-17 16-32-01](https://user-images.githubusercontent.com/71149420/126038716-3d23eb72-6e17-474d-a45b-d21e367e9303.png)
"/></kbd>


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## TravisCI
[![Build Status](https://travis-ci.com/dnplkv/hw5_Polyakov.svg?branch=lint_br)](https://travis-ci.com/dnplkv/hw5_Polyakov)
