web: python manage.py runserver
web: gunicorn collabio.wsgi:application --log-file -
heroku ps:scale web=1