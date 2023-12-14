from django.contrib import admin
from .models import Enviado
# Register your models here.


@admin.register(Enviado)
class GestionEnviado(admin.ModelAdmin):
    list_display = ( 'coddoc','title','status', 'type_doc', 'observacion' )
    list_filter = ('status', 'type_doc',)
    search_fields = ('coddoc', )
    list_display_links = ('coddoc',)
    list_per_page = 5
