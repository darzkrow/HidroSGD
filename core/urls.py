
from django.contrib import admin
from django.urls import path, include, re_path
from .views import Inicio
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Inicio.as_view(), name = 'index'),
    path('', include('accounts.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)