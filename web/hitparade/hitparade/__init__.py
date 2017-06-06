# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app


__about__ = """
In addition to what is provided by the "zero" project, this project
provides thorough integration with django-user-accounts, adding
comprehensive account management functionality. It is a foundation
suitable for most sites that have user accounts.
"""

default_app_config = "hitparade.apps.AppConfig"


__all__ = ['celery_app']
