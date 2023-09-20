FROM python:3.11-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD echo "Начинаю выполнение скрипта..."
ENTRYPOINT ["python", "main.py"]
