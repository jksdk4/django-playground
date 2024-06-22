from django.urls import path

from . import views

urlpatterns = [
    # removing 'home' here and naming this as home won't throw the initial
    # page error on :8080; it will now point to the welcome.html page
    path('', views.HomeView.as_view(), name="home"),
    path('login', views.LoginInterfaceView.as_view(), name="login"),
    path('logout', views.LogoutInterfaceView.as_view(), name="logout"),
    path('signup', views.SignupView.as_view(), name="signup"),
]
