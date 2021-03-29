from django.urls import path
from . import viewsAdmin

urlpatterns = [
    path('index', viewsAdmin.index, name='indexAdmin'),
    path('create', viewsAdmin.create, name='createAdmin'),
]