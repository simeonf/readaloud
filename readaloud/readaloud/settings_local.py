from .settings import *  # noqa: F403

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_extensions",
    ] + MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]
