FROM python:3.7.3-stretch

RUN useradd dispenser

WORKDIR /home/dispenser

COPY index.html ./
COPY script.js ./

EXPOSE 8000
ENTRYPOINT python -m http.server 8000