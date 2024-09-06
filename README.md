# SNCTE-DB
1- Generar imagen Docker:
docker build -t sncte-db:latest .

2- En bash correr:
docker run -d --name flask-vue -p 5000:8000 -v c:/Users/esartor/Desktop/Dev/db-radiolocalizacion/backend/instance:/app/instance sncte-db:latest

3- Dentro del contenedor, correr nginx con el siguiente comando:
nginx -c /etc/nginx/default.conf