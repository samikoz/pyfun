FROM node:8-jesse

RUN useradd front

WORKDIR /home/front

COPY . .
RUN npm install

EXPOSE 8000
ENTRYPOINT node index.js