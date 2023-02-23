from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('contacts', views.contacts),
    path('secret', views.secret),
]
