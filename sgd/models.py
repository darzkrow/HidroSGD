from django.db import models
from django.contrib.auth.models import User


class Correspondence(models.Model):
    id = models.AutoField(primary_key=True)
     # Agregar campo para el estado de la correspondencia
    STATUS_CHOICES =  [
        ('ABIERTO', 'ABIERTO'),
        ('CERRADO', 'CERRADO'),
        ('EXPIRADO', 'EXPIRADO'),
        ]
    status = models.CharField('Estado de la Doc.',max_length=20, 
                  choices=STATUS_CHOICES, 
                  default='ABIERTO')

    TYPE_CHOICES =  [
        ('CIRCULAR', 'CIRCULAR'),
        ('INFORME', 'INFORME'),
        ('OFICIO', 'OFICIO'),
        ('NOTA_DE_ENTREGA', 'NOTA DE ENTREGA'),
        ('NOTA_DE_SALIDA', 'NOTA DE SALIDA'),
        ('PUNTO_DE_CUENTA', 'PUNTO DE CUENTA'),
        
        ]
    type_doc = models.CharField('Tipo de Documento',max_length=20,
                    choices=STATUS_CHOICES, 
                    default='MEMORANDO')


    observacion = models.TextField(
        'Observaciones', max_length=255,  null=True, blank=True)
    
    create_at = models.DateField(
        'Fecha de Creacion', auto_now=False, auto_now_add=True)
    update_at = models.DateField(
        'Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_at = models.DateField(
        'Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    created_by_user = models.ForeignKey(
        User,
        verbose_name='Creado Por',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    class Meta:
        abstract = True


class Enviado(Correspondence):
    title = models.CharField('Titulo',max_length=100)
    coddoc = models.CharField('Codigo', max_length=50, null=False, blank=False)
    docENV = models.FileField(null=True, blank=True, upload_to='empresa/doc')


    class Meta:
        verbose_name = 'Correspondencia Enviada'
        verbose_name_plural = 'Correspondencias Enviadas'
        db_table = 'sgd_env'

    


