# Описание

Данный репозиторий создан в целях обучения. Модуль от [devman](https://dvmn.org/modules/django-orm/)

P.S мой код делает только выборку данных из бд

## Как запустить

1. Установить python3

```sh
sudo apt-get install python3
sudo apt-get install python3-pip
```

2. Скачать проект и установить зависимости

```sh
git clone https://github.com/Safintim/dvmn-django-orm-control-bank
cd dvmn-django-orm-control-bank
pip3 install -r requirements.txt
```

3. Требуется создать .env файл, с персональными настройками ввида:

```.env
DB_HOST=your_host
DB_PORT=your_port
DB_NAME=your_name
DB_USER=your_username
DB_PASSWORD=your_password
SECRET_KEY=your_secret_key
```

4. Запустить проект

```sh
python3 manage.py runserver
```

Перейти по адресу http://127.0.0.1:8000/