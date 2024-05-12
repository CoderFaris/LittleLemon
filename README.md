# LittleLemon
This is a Back-end capstone project that required me to:
- Connect the Little Lemon restaurant back-end to MySQL
- Set up the Little Lemon restaurant booking api
- Insert booking data in the database via the booking API

# How to run it
(install python first and the required libs if you don't have it on your pc)
```
#create a virtual env using pipenv
pipenv shell

pipenv install django
pipenv install djangorestframework
pipenv install djoser
pipenv install mysqlclient
```

```
create database littlelemon;
use littlelemon;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'django'@'localhost';
```

```
python3 manage.py migrate 
python3 manage.py makemigrations
python manage.py createsuperuser
#user:super
#email: super@gmail.com
#password: 123
```

Requests: GET or POST (authorized users only)
```
api/menu
```

Requests: GET, PUT or DELETE
```
api/menu/{id} (2 you can input as an example)
```

Requests: GET or POST (authorized users only)
```
api/booking/tables
```

Requests: GET, PUT or DELETE (authorized users only)
```
api/booking/tables/{id} (same for here)
```

Requests: POST (valid credentials)
```
api/api-token-auth/
```

Requests: GET (html page)
```
home/
```

Rest of the API endpoints are from Djoser

#Testing
```
python manage.py test
```
In order to test API endpoints, you must have either Postman, Insomnia, Curl or any other tool for API endpoint testing.

