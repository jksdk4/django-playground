from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/welcome.html', {})

@login_required(login_url='/admin')     # if I try to go to /authorized and am not signed in, redirect to admin login
def authorized(request):
    return render(request, 'home/authorized.html', {})