# Generated by Django 4.2.5 on 2023-11-10 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_solicitud_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='fecha_notificacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]