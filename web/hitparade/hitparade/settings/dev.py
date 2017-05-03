"""Development settings and globals."""
# See: https://docs.djangoproject.com/en/dev/ref/settings/

import os

from .base import *
from .dev import *

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': get_env_variable('MYSQL_HOST'),
        'PORT': get_env_variable('MYSQL_PORT'),
        'USER': get_env_variable('MYSQL_HP_USER'),
        'PASSWORD': get_env_variable('MYSQL_PASSWORD'),
        'NAME': get_env_variable('MYSQL_DATABASE'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        }
    },
}
