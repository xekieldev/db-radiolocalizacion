#!/bin/sh

# Iniciar Flask en segundo plano
.venv/bin/flask --app src run --debug &

# Iniciar Nginx en el primer plano
nginx -c /etc/nginx/default.conf -g 'daemon off;'
