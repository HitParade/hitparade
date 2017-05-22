FROM node:7.10.0-alpine

RUN mkdir -p /code/

ADD hitparade/ /code/
WORKDIR /code

RUN npm install

CMD ["/usr/local/bin/npm run watch"]
