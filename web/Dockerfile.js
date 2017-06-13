FROM node:7.10.0-alpine

RUN mkdir -p /code/

ADD hitparade/ /code/

ADD package.json ./
WORKDIR /code

RUN npm install

CMD ["/usr/local/bin/npm run start"]
