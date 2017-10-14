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
$ pip instal -r requirements/base.txt
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


### Upgrades and migrations

Upon deploying the new code it will sometimes become necessary to perform
database migrations, like so:

```
$ cd ~/where/your/project/lives
$ source ~/.venv/geekbeacon/bin/activate 
$ python manage migrate
```
And that's basically it.


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


### Deployment in production

Right now we're in early stages, so I would rather not over-engineer things too much.
Install Nginx, PostgresSQL, gunicorn and supervisord. In the deploy directory are config templates
for Nginx, supervisord and Django/wagtail and a sample credentials file.

Pre-deployment checks:

 - create a geek beacon dedicated user
 - create `/home/user/credentials/geekbeacon_settings.py` theres's an example file in deploy directory

When deploying these steps should be perfomed:

 - switch to the geek beacon dedicated user
 - go to the base directory where you want everything installed, I used `/srv` in all the examples
 - git clone/pull the latest sources, either master or select by tag, whatever
 - run deploy.py script
 - start python virtual env, usually by `source /srv/.venv/bin/activate`
 - install all the requirements `pip install --no-cache-dir -r requirements.txt`
 - perform django database migrations `python manage.py migrate`
 - collect django static files `python manage.py collectstatic --clear --no-input`
 - tell supervisord to restart gunicorn processes `supervisorctl signal HUP all`
   - if sueprvisord is taking care of other stuff, not just gunicorn, then 'all' parameter might not be a good idea
   
**Make sure to check and double check those scripts. They are not tested, they were taken from some production server
and hacked a bit for geekbeacon. You'll probably have to fix them.**



### TODO

- make front page more dynamic, currently in progress
- --write some-- improve deployment docs
- ...
- profit
