from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
    
    
class AuthorizedView(TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
