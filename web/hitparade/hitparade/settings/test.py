"""Development settings and globals."""
# See: https://docs.djangoproject.com/en/dev/ref/settings/

import os

from .base import *

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'hitparade.db'),

    }
}

INSTALLED_APPS = INSTALLED_APPS + ['django_nose']

########## TEST CONFIGURATION
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--nocapture',
    '--nologcapture',
    '--with-coverage',
    '--cover-package=hitparade',
    '--with-ddf-setup'
]
DDF_DEFAULT_DATA_FIXTURE = 'sequential'
########## END TEST CONFIGURATION

