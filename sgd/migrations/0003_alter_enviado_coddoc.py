# Generated by Django 5.0 on 2023-12-14 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgd', '0002_alter_enviado_docenv_alter_enviado_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enviado',
            name='coddoc',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Codigo'),
        ),
    ]