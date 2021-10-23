from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


MIDDLEWARE += (
    'livereload.middleware.LiveReloadScript',
)
INSTALLED_APPS += [
    'livereload',
]