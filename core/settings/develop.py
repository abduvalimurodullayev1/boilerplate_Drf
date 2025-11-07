from .base import *  # noqa

DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]

CELERY_TASK_ALWAYS_EAGER = False

INTERNAL_IPS = ["127.0.0.1"]


ALLOWED_HOSTS = ["*"]
