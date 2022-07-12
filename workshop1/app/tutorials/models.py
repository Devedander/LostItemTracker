from django.db import models

# Create your models here.
class Lost_Items(models.Model):
    item = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    date_found = models.CharField(max_length=200, blank=False, default='')
    lcation_found = models.CharField(max_length=150, blank=True, null=True)
    recovered = models.BooleanField(default=False)