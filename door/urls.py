from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('', views.door),
    path('fail', views.fail),
    path('login', v.LoginView.as_view(), name='login'),
    path('reg', views.reg),
]