from .settings import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "readaloud",
        "OPTIONS": {
            "read_default_file": "/home/ubuntu/my.cnf",
        },
    }
}


ALLOWED_HOSTS = ["*"]

STATIC_ROOT = "/var/www/apps/readaloud/static"

MEDIA_ROOT = "/var/www/apps/readaloud/media"

DEBUG = False
