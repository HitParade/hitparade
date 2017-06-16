FROM node:7.10.0-alpine

RUN mkdir -p /code/
WORKDIR /code

ADD hitparade/ /code/

RUN npm install

CMD ["/usr/local/bin/npm run start"]
