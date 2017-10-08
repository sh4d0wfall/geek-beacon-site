Geek Beacon - DEVELOPMENT GUIDE
===============================

This proejct is setup and tightly coupled with docker.  If you're not familiar with docker please visit https://www.docker.com/ to learn more.

Requires: docker, docker-compose.

Please read over this section for more details:  http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


The web applicatin is created using the following technologies:

- Django - backend web service
- Postgres - Database for persistenace
- Bootstrap 4, CSS, HTML etc.

Django Configuration
--------------------

Based on cookiecutter django project, most settings are detailed here:  http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ docker-compose -f local.yml run django python manage.py createsuperuser

  For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


* To migrate the database models when needed::
    $ docker-compose -f local.yml run django python manage.py makemigrations
    $ docker-compose -f local.yml run django python manage.py migrate


Content Administraion
^^^^^^^^^^^^^^^^^^^^^
* The content administration pages are restricted to anyone in the 'Editor' group. You will need to create this group through the Django Admin.



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd geek_beacon
    celery -A geek_beacon.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.



