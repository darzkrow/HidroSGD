from django.contrib import admin
from .models import Enviado, Recibido, SeguimientosEnv
# Register your models here.


@admin.register(Enviado)
class GestionEnviado(admin.ModelAdmin):
    readonly_fields = ('coddoc',)
    list_display = ( 'coddoc','title','status', 'type_doc', 'observacion', 'create_at' )
    
    list_filter = ('status', 'type_doc',)
    search_fields = ('coddoc', )
    list_display_links = ('coddoc',)
    list_per_page = 10



@admin.register(Recibido)
class GestionRecibido(admin.ModelAdmin):
    list_display = ( 'coddoc','title','status', 'type_doc', 'observacion', 'create_at' )
    list_filter = ('status', 'type_doc',)
    search_fields = ('coddoc', )
    list_display_links = ('coddoc',)
    list_per_page = 10


@admin.register(SeguimientosEnv)
class GestionSeguimientosEnv(admin.ModelAdmin):
    list_display = ( 'SegEnv','author')
 