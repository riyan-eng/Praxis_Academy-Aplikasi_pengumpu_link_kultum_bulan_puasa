from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.timeSchedule)
class timeSchedule(admin.ModelAdmin):
  list_display = ('name', 'time')

@admin.register(models.schedule)
class schedule(admin.ModelAdmin):
  list_display = ('user', 'date', 'time', 'lector', 'topic', 'description', 'link', 'tag')