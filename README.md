## Запуск с помощью Docker:

Клонируйте репозиторий: `git clone https://github.com/Bigbear2006/sudact.git`  
Cоздайте файл .env со следующими переменными:
```
POSTGRES_DB = <название базы данных>
POSTGRES_USER = <имя пользователя>
POSTGRES_PASSWORD = <ваш пароль>
```
Соберите образ Docker: `docker build .`  
Запустите Docker: `docker-compose up`  
Скрипт выведет результаты в консоль

## Запуск скрипта без Docker:

Создайте виртуальную среду, активируйте её и установите нужные библиотеки:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install psycopg2
```

Создайте файл .env со следующими переменными:
```
POSTGRES_DB = <название базы данных>
POSTGRES_USER = <имя пользователя>
POSTGRES_PASSWORD = <ваш пароль>
POSTGRES_HOST = localhost или <ваш хост>
POSTGRES_PORT = 5432 или <ваш порт>
```

Запустите скрипт:
`python main.py`  
Скрипт выведет результаты в консоль