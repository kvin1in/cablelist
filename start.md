###После распаковки, внутри этой папки
pipenv shell

pipenv install

pipenv run pip install psycopg2

/journal/settings.py <- Изменить настройки DATABASES

python manage.py inspectdb > models.py

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

python manage.py createsuperuser





###Добавление, удаление и тп
http://localhost:8000/admin

Login: admin

pw: admin

Все во вкладке Items