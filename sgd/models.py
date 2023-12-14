from django.db import models

# Create your models here.

class Enviado(models.Model):
    uuid = models.UUIDField()
    fecha_doc = models.DateField()
    referencia = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=255)
    estado = models.CharField(max_length=100, null=True, default='NO ESPECIFICADO')
    otro = models.CharField(max_length=255)
    estatus = models.CharField(max_length=100)
    fecha_rec = models.DateField()
    file = models.CharField(max_length=255)
    nro_doc = models.CharField(max_length=255, null=True, default='0')
    tipo_doc = models.CharField(max_length=100)
    recibido_por = models.CharField(max_length=255)
    accion = models.CharField(max_length=100)
    bandeja_de = models.CharField(max_length=100)
    seguimiento = models.CharField(max_length=255)
    active = models.IntegerField(null=True, default=1)

    codigo = models.CharField(max_length=255)
    tipo_c = models.IntegerField()

    # Extras
    ref_doc = models.CharField(max_length=255, null=True)
    fecha_lim = models.DateField(null=True)
    ccopia = models.CharField(max_length=255, null=True)

    # Definir las relaciones con los usuarios si es necesario
    # id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id_user_destino = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'enviados'  # Nombre de la tabla en la base de datos


class Recibido(models.Model):
    tipo = models.CharField(max_length=100)
    uuid = models.UUIDField()
    remitente = models.CharField(max_length=255)
    estado = models.CharField(max_length=100, null=True, default='NO ESPECIFICADO')
    otro = models.CharField(max_length=255)
    recibido_por = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    tipo_doc = models.CharField(max_length=100)
    fecha_doc = models.DateField()
    nro_doc = models.CharField(max_length=255)
    estatus = models.CharField(max_length=100)
    accion = models.CharField(max_length=100)
    seguimiento = models.CharField(max_length=255)
    active = models.IntegerField(null=True, default=1)

    bandeja_de = models.CharField(max_length=100)
    codigo = models.CharField(max_length=255)
    tipo_c = models.IntegerField()

    # Extras
    ref_doc = models.CharField(max_length=255, null=True)
    fecha_lim = models.DateField(null=True)
    # id_user_destino = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recibidos'  # Nombre de la tabla en la base de datos




class Seguimiento(models.Model):
    id_documento = models.IntegerField()
    id_usuario = models.IntegerField()
    accion = models.CharField(max_length=255)
    fecha = models.DateField()
    bandeja_de = models.IntegerField()
    instruccion = models.CharField(max_length=255)
    estatus = models.CharField(max_length=255)
    tipo_c = models.IntegerField()
    # seguimiento = models.CharField(max_length=255)  # Si es necesario agregar este campo

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'seguimientos' 