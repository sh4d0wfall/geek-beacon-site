#!/usr/bin/python3

import os
import fileinput
import importlib.util

# Find configuration file and load it
f = os.path.expanduser('~') + '/credentials/geekbeacon_settings.py'
spec = importlib.util.spec_from_file_location('Credentials', f)
credentials = importlib.util.module_from_spec(spec)
spec.loader.exec_module(credentials)

# Prepare replacements
replace = [('##DBNAME##', credentials.DB_NAME),
           ('##DBUSER##', credentials.DB_USER),
           ('##DBPASS##', credentials.DB_PASS),
           ('##DBHOST##', credentials.DB_HOST),
           ('##MEDIADIR##', credentials.MEDIA_DIR),
           ('##STATICDIR##', credentials.STATIC_DIR),
           ('##SECRETKEY##', credentials.SECRET_KEY),
           #
           # Nginx settings
           #
           ('##DJANGODIR##', credentials.DJANGO_DIR),
           ('##GUNICORNSOCKDIR##', credentials.GUNICORN_SOCK),
           ('##SSLCERTIFICATE##', credentials.SSL_CERTIFICATE),
           ('##SSLKEY##', credentials.SSL_KEY),
           ('##VENVDIR##', credentials.VENV_DIR)

           ]

# Replace, REPLACE!
with fileinput.FileInput('../geekbeacon/settings/production.py', inplace=True, backup='.bak') as file:
    for l in file:
        for s, r in replace:
            l = l.replace(s, r)
        print(l, end='')

with fileinput.FileInput('geekbeacon-site', inplace=True, backup='.bak') as file:
    for l in file:
        for s, r in replace:
            l = l.replace(s, r)
        print(l, end='')

with fileinput.FileInput('gunicorn_start.sh', inplace=True, backup='.bak') as file:
    for l in file:
        for s, r in replace:
            l = l.replace(s, r)
        print(l, end='')
