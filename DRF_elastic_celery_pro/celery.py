# project_name/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_elastic_celery_pro.settings')

app = Celery('DRF_elastic_celery_pro')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()    # automatically detect tasks.py file from all apps.

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))