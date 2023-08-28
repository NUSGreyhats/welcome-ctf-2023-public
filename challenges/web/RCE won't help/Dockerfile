FROM python:3.11

WORKDIR /app

COPY --chown=www-data:www-data app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

USER www-data

CMD ["python3","app.py"]
