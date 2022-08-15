release: python manage.py migrate 
web: gunicorn priceCompare.wsgi --log-file--
web: python priceCompare/priceCompare/manage.py runserver 0.0.0.0:$PORT