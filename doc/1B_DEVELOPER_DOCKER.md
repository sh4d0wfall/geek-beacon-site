## Docker Method


If you're not familiar with docker you can learn more about docker [here](http://www.docker.com/).

There are two configuration files one titled local.yml and another titled production.yml

For development purposes you can completely ignore production.yml so my suggestion is to simply create 
an alias to local.

``` 
ln -s local.yml docker-compose.yml
```

The database credentials are configured in local.yml.  

Simply build the containers by running:

``` 
docker-compose build
```

Bring up the containers:


``` 
docker-compose up -d 
``` 


Then follow the logs if you like:

``` 
docker-compose logs -f 
``` 


Create your super user:

``` 
docker-compose run django python manage.py migrate  ## this should not be needed
docker-compose run django python manage.py createsuperuser
``` 


## Debugging:

http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html


https://www.youtube.com/watch?v=n-wwp17MqhU Possibly useful. 
