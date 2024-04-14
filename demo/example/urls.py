from django.urls import path

from . import views

urlpatterns = [
    path('list-notes', views.list_notes),
    path('list-images', views.list_images),
    path('list-both', views.list_both)
]
