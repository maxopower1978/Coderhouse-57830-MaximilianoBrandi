# Generated by Django 5.1.1 on 2024-09-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_alter_consulta_fecha_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha_respuesta',
            field=models.DateField(),
        ),
    ]
