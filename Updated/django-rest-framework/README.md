# How to view lecture materials
* Open current path in terminal and run a Python server so that Python server can see remark HTML files.

```
python -m SimpleHTTPServer 8080
```

Then visit below remark slide urls

* [Introduction to REST API](http://localhost:8080/intro_remark.html)
* [Django REST Framework](http://localhost:8080/rest_framework_remark.html)

# Project setup

* ```sudo easy_install pip``` (Install pip first if you don't have one)
* ```sudo pip install virtualenv virtualenvwrapper``` (Install the virtual environment)
* Add this code to ~/.profile or ~/.bash_rc. Then restart the terminal to take effect.
* ```source /usr/local/bin/virtualenvwrapper.sh```
* ```mkvirtualenv todoList``` (Create a virtual environment)
* ```workon todoList``` (Goes into a virtual environment)
* ```pip install -r requirements.txt```
* ```django-admin startproject todoList```
* ```cd todoList``` (Go into the project folder)
* ```python manage.py migrate```
* ```python manage.py runserver```

# Assignments
* [Django REST Framework Workshop Assignments](exercises.md)

# Additional resources
* [Django REST Framework Offical Website](http://www.django-rest-framework.org/)

# django-cors-headers package setup
For the Single-Page-Application full-stack architecture, the usual idea is to run your Django RESTful API application at one port and your SPA web application at a different port. Because they are in same domain URL at different ports, they are considered different domain URLs. In order to talk to each other in same url but different ports, we need to use a technique called **Cross-Origin Resource Sharing**.

1. Install django-cors-headers package to your todo Django project's virtual environment.
    ```
    pip install django-cors-headers
    ```
2. Add django-cors-headers app to your Django settings' INSTALLED_APPS.
   ```
INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)
   ```
3. Add CorsMiddleware above Django's CommonMiddleware.
```
MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)
```
4. Add the rest of CORS header Django settings.

```
CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'Api-Authorization',
)
```

Now your SPA app can communicate to your Django RESTful API endpoints!
