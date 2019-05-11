FROM node:8-jessie

RUN useradd front

WORKDIR /home/front

COPY . .
RUN npm install

EXPOSE 8000
ENTRYPOINT node index.js
