FROM python:3.7.3-stretch

RUN useradd dispenser

WORKDIR /home/dispenser

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP main.py

EXPOSE 5000
ENTRYPOINT flask run --host=0.0.0.0