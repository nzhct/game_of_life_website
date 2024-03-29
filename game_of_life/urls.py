from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from door.views import reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('door.urls')),
    path('game/', include('game.urls')),
    path('about/', include('about.urls')),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

