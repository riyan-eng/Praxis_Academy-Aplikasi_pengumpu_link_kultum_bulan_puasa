from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import formsAccount
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def register(req):
    form = formsAccount.createUser()
    if req.method == 'POST':
        form = formsAccount.createUser(req.POST)
        if form.is_valid():
            form.save()
    return render(req, 'accounts/register.html',{
        'form': form,
    })

def login(req):
    if req.user.is_authenticated:
	    return redirect('indexAdmin')
    else:
        if req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = authenticate(req, username= username, password= password)
            if user is not None:
                auth_login(req, user)
                return redirect('indexAdmin')
        return render(req, 'accounts/login.html')

def logout(req):
    auth_logout(req)
    return redirect('/accounts/login')