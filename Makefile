requirements:
	pip install -r requirements.txt

make-migrations:
	python manage.py migrate

migrate:
	python manage.py migrate

run:
	python manage.py runserver
