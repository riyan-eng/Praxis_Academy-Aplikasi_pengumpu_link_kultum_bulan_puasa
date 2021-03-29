from django.db import models
from django.contrib.auth.models import User
from datetime import date

class timeSchedule(models.Model):
    name = models.CharField(max_length=50)
    time = models.TimeField(blank=True)
    def __str__(self):
        return self.name

class schedule(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name='pesantren')
    date = models.DateField(default=date.today)
    time = models.ForeignKey(timeSchedule, on_delete=models.CASCADE, related_name='waktu')
    lector = models.CharField(max_length=125)
    topic = models.CharField(max_length=125)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)