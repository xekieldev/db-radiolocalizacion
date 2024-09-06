# build
FROM node:20 as build-vue
WORKDIR /data
COPY ./data .
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./frontend/package*.json ./
RUN npm install
COPY ./frontend .
RUN npm run build

# production
FROM nginx:mainline-alpine as production
WORKDIR /app
RUN apk --no-cache add make gcc g++
# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 python3-dev py3-greenlet && ln -sf python3 /usr/bin/python
RUN apk add --update --no-cache py3-pip
RUN apk update && apk add --no-cache sqlite
COPY --from=build-vue /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/default.conf
COPY ./backend .
RUN rm -r instance
RUN python -m venv .venv
RUN .venv/bin/pip install -e .
RUN .venv/bin/pip install -r requirements.txt
CMD .venv/bin/flask --app src run --debug && nginx -c /etc/nginx/default.conf

