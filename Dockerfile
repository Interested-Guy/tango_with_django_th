FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY tango_with_django_project .

RUN python3.9 manage.py makemigrations

RUN python3.9 manage.py migrate

EXPOSE 8000

CMD [ "python3.9", "manage.py", "runserver", "0.0.0.0:8000"]
