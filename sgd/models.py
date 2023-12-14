from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


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
                    choices=TYPE_CHOICES, 
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
    coddoc = models.CharField('Codigo', max_length=50, null=True, blank=True)
    docENV = models.FileField(null=True, blank=True, upload_to='doc/enviada')


    class Meta:
        verbose_name = 'Correspondencia Enviada'
        verbose_name_plural = 'Correspondencias Enviadas'
        db_table = 'sgd_env'# Función para generar el valor del campo 'coddoc' antes de guardar el objeto Enviado

    def __str__(self):
        return self.coddoc
    
@receiver(pre_save, sender=Enviado)
def generate_coddoc(sender, instance, **kwargs):
    if instance.coddoc is None or instance.coddoc == '':
        last_enviado = Enviado.objects.filter(coddoc__startswith='DOC-').order_by('-id').first()

        if last_enviado:
            last_coddoc = int(last_enviado.coddoc[4:])  # Extraer el número después de 'DOC'
            new_coddoc = f'DOC-{last_coddoc + 1:4}'  # Incrementar el número y formatear con ceros a la izquierda
        else:
            new_coddoc = 'DOC-0001'  # Si no hay correspondencias anteriores, iniciar desde 'DOC0001'

        instance.coddoc = new_coddoc

 
    

class Recibido(Correspondence):
    title = models.CharField('Titulo',max_length=100)
    coddoc = models.CharField('Codigo', max_length=50, null=False, blank=False)
    docREC = models.FileField(null=True, blank=True, upload_to='doc/recibido')


    class Meta:
        verbose_name = 'Correspondencia Recibida'
        verbose_name_plural = 'Correspondencias Recibids'
        db_table = 'sgd_rec'




class SeguimientosEnv(models.Model):    
    SegEnv = models.ForeignKey(Enviado, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username}"