web: python manage.py runserver
web: gunicorn collabioproject/collabio/wsgi:application --log-file -
heroku ps:scale web=1