## Steps to run

 ``docker run -d --name=test -p 8000:8000 dockercoolexp/tango_django:v1``
 
 Goto localhost:8000
 
 1. For Search functionality in Add Category: ``docker exec -it test bash``. Create a serpapi account and obtain the api key. Paste the key using echo: ``echo <key> > serpapi.key
 2. For creating superuser:
    1. ``docker exec -it test bash``
	2. `` python manage.py createsuperuser``
	3. Goto localhost:8000/admin and authenticate using the newly created credentials.