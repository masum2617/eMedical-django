release: python manage.py migrate 
release: heroku run python manage.py loaddata project_dump.json
web: gunicorn eMedical.wsgi