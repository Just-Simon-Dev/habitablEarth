FROM --platform=$BUILDPLATFORM node:17.0.1-bullseye-slim as builder

RUN mkdir /habitablEarth
WORKDIR /habitablEarth

RUN npm install -g @angular/cli@15

COPY ./habitablEarth/package.json ./habitablEarth/package-lock.json ./
RUN npm ci


COPY ./habitablEarth/. .
CMD ["ng", "serve", "--host", "0.0.0.0"]