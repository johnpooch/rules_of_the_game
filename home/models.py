from django.db import models
from django.utils import timezone
# import datetime


class Rule(models.Model):
    description = models.CharField(max_length=1000, default='')
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
