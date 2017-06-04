from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

app = Celery('hitparade')

CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


