from django.urls import path
from . import views

urlpatterns = [
    path('', views.door),
    path('fail', views.fail),
]