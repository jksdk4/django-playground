from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = 'smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"


# LogoutView is deprecated as of Django 5.
# This will not redirect.
class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
    
    
class AuthorizedView(TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
