from __future__ import absolute_import, unicode_literals
import os

from celery import Celery 
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pharma.settings')

app=Celery('pharma')
app.conf.enable_utc = False

app.conf.update(timezone='Aisa/Kolkata')

app.config_from_object(settings,namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'core.tasks.send_mail_func',
        'schedule': crontab(hour=11, minute=44),
        #'args': (2,)
    },
    'send-sms-every-day-at-8': {
        'task': 'core.tasks.send_sms',
        'schedule': crontab(hour=11, minute=44),
        #'args': (2,)
    }, 
}
    
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')