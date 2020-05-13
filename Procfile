heroku ps:scale web=1
web: python manage.py runserver
web: gunicorn collabio.wsgi:app --log-file -