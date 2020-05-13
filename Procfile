web: python manage.py runserver
web: gunicorn collabio:application --log-file -
heroku ps:scale web=1