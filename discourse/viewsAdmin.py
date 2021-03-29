from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import formsAdmin

@login_required(login_url='login')
def index(req):
    return render(req, 'admin/dashboard.html')

@login_required(login_url='login')
def create(req):
    form = formsAdmin.createSchedule()
    if req.POST:
        form_input = formsAdmin.createSchedule(req.POST)
        if form_input.is_valid():
            form_input.instance.user = req.user
            form_input.save()
        return redirect('indexAdmin')
    return render(req, 'admin/create.html',{
        'form': form,
    })
