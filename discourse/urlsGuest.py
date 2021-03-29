from django.urls import path
from . import viewsGuest

urlpatterns = [
    path('', viewsGuest.index, name='indexGuest')
]