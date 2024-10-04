# production
FROM nginx:mainline-alpine as production
WORKDIR /app
RUN apk --no-cache add make gcc g++
# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 python3-dev py3-greenlet && ln -sf python3 /usr/bin/python
RUN apk add --update --no-cache py3-pip
RUN apk update && apk add --no-cache sqlite
# COPY --from=build-vue /app/dist /usr/share/nginx/html
# COPY ./nginx/default.conf /etc/nginx/default.conf
COPY ./ .
RUN rm -r instance
RUN python -m venv .venv
RUN .venv/bin/pip install -e .
RUN .venv/bin/pip install -r requirements.txt
# CMD .venv/bin/flask --app src run --debug
COPY ./nginx/default.conf /etc/nginx/default.conf
WORKDIR /script
COPY ./script/run.sh /app/run.sh
WORKDIR /app
RUN chmod +x /app/run.sh
CMD ["/bin/sh", "/app/run.sh"]