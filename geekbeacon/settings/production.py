from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = '##SECRETKEY##'

MEDIA_ROOT = '##MEDIADIR##'
STATIC_ROOT = '##STATICDIR##'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '##DBNAME##',
        'USER': '##DBUSER##',
        'PASSWORD': '##DBPASS##',
        'HOST': '##DBHOST##',
        'PORT': '',
    }
}
