# build
FROM node:20 as build-vue
WORKDIR /data
COPY ./data .
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./package*.json ./
RUN npm install
COPY ./ .
RUN npm run build

FROM nginx:1.13-alpine
COPY --from=build-vue /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/default.conf
# CMD nginx -c /etc/nginx/default.conf
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/default.conf"]