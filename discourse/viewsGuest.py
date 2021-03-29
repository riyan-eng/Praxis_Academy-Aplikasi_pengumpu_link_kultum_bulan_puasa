from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(req):
    data = models.schedule.objects.all()
    return render(req, 'guest/index.html',{
        'data': data,
    })