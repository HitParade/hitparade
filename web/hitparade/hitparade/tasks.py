from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def debug_task(x, y):
    print "debug_task"
    print x
    print 7
    return x + y
