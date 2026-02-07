web: gunicorn portfolio.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && python manage.py createsuperuser && gunicorn portfolio.wsgi