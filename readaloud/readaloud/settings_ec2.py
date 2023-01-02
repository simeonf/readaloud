from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "/home/ubuntu/my.cnf",
        },
    }
}


ALLOWED_HOSTS = ['*']

STATIC_ROOT = "/var/www/apps/readaloud/static"
