FROM node:16.13.0-alpine as builder
COPY ./habitablEarth /app
WORKDIR /app

RUN npm install
RUN npm run build

FROM nginx:1.17.10-alpine
EXPOSE 80
COPY ./nginx/default.conf /etc/nginx/conf.d/

COPY --from=builder /app/dist/habitabl-earth /usr/share/nginx/html