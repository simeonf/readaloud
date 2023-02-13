from .settings import *  # noqa: F403

INSTALLED_APPS += [  # noqa: F405
    "django_extensions",
    "debug_toolbar"]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE  # noqa: F405

INTERNAL_IPS = [
    "127.0.0.1",
]
