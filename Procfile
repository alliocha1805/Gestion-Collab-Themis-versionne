web: gunicorn collabio.wsgi:app --log-file -
web: python manage.py runserver
heroku ps:scale web=1