from django.urls import path
from . import viewsAccounts

urlpatterns = [
    path('register/', viewsAccounts.register),
    path('login/', viewsAccounts.login, name= 'login'),
    path('logout/', viewsAccounts.logout, name='logout'),
]