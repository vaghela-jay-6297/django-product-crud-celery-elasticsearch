from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from DRF_elastic_celery_pro.celery import app as celery_app

__all__ = ('celery_app',)   # inintalize celery app when user run the project
