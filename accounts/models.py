from django.db import models

# Create your models here.


class ConfiguracionPagina(models.Model):
    titulo = models.CharField(max_length=100)
    ruta_logo = models.CharField(max_length=200)  # Aquí podrías usar un campo de imagen si lo prefieres

    def __str__(self):
        return self.titulo