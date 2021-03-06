from __future__ import absolute_import, unicode_literals

import logging
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from celery.signals import setup_logging
from celery.utils.log import get_task_logger

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insurance_management.settings')
app = Celery('insurance_management')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.conf.enable_utc = False
app.conf.update(timezone='Asis/Kolkata')
app.config_from_object(settings, namespace="CELERY")

app.conf.beat_schedule = {
    'trigger_mail_reminder_everyday_at_10_A.M': {
        'task': 'insurance.tasks.remind_insurances',
        'schedule': crontab(hour=16, minute=55),
    },

}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))