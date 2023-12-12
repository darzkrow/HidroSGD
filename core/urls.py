from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from .views import Inicio
from django.conf.urls.static import static



from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Inicio.as_view(), name = 'index'),
     re_path(r'^favicon\.ico$', favicon_view),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

