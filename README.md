## Geek Beacon


Website, built on wagtail


### Setting up development environment

Choose a Linux distribution you prefer. Make sure that:

- Python 3.4 at least needs to be installed
- Make sure that venv is also installed, it usually is

First you need to setup your virtual environment:

```
$ mkdir -p ~/.venv/geekbeacon
$ python3 -m venv ~/.venv/geekbeacon
$ sudo apt-get install python3-pip      # Just in case
```

Now, activate the environment and complete installation there:

```
$ source ~/.venv/geekbeacon/bin/activate
$ pip install wheel
$ pip install wagtail
```

Create a directory for your site and clone the github repo:

```
$ mkdir ~/GeekBeacon
$ cd ~/GeekBeacon
$ git clone git@github.com:OSAlt/geek-beacon-site.git .
```

Now all you have to do is to install the requirements and create superuser:

```
$ pip instal -r requirements.txt
$ pyhton manage.py migrate
$ python manage.py createsuperuser
```

Once you have a superuser you can start the site and try if it works:

```
$ python manage.py runserver
```

At last, you will have to create the default site. Start by logging into admin interface at
at http://127.0.0.1:8000/admin/

In the left hand menu select Pages and then again Pages. Add new child page and make sure
you select Home Page type. Give it a nice title and publish it. Now delete the default Welcome page.
Go to the Settings and select Sites. Add a site. Use localhost as a hostname and also give it a nice name. :)

Select a root page. There should be only one page available. Check 'Is default site:' and save the site.

Point your browser to http://127.0.0.1:8000 and it should be working.

Now you can start adding pages, blog index pages and blog posts.

Categories are hidden in the Snippets menu.


### Setting up stuff
#### Footer section

Right now there are 4 categories hardcoded in the `footer.html` template:

- geeks-abroad
- gaming
- osalt
- squirrel-army

This means that these categories have to exist and their _slugs_, have
to be the same as on this list. If they are not, then posts in those
categories won't be shown in the footer.  

#### TBD

Etc, etc, &hellip;


### TODO

- make front page more dynamic, currently in progress
- ...
- profit

