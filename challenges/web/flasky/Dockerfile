FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src .
RUN chown -R root:root /python-docker && \
    chmod -R 555 /python-docker && \
	mkdir /python-docker/instance && \
	chmod 777 /python-docker/instance

USER www-data
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
