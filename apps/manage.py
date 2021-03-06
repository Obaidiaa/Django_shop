#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} envirment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)

if __name__ == '__main__':
    """Run administrative tasks."""

    DJANGO_EXECUTION_ENVIRONMENT = get_env_variable('DJANGO_EXECUTION_ENVIRONMENT')
    if(DJANGO_EXECUTION_ENVIRONMENT == 'LOCAL'):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings.local")
    if(DJANGO_EXECUTION_ENVIRONMENT == 'PRODUCTION'):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE","conig.settings.production")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)