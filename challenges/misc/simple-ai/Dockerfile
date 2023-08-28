FROM ubuntu:latest

WORKDIR /app

COPY ./app/chall.py /app/chall.py

RUN apt-get update && \
    apt-get install -y python3 python3-pip socat

RUN pip3 install torch

RUN chown -R root:root /app && \
    chmod -R a-w /app

USER www-data
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:"python3 /app/chall.py"