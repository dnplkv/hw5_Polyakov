FROM nginx:1.20


RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY proxy_params /etc/nginx/conf.d/proxy_params