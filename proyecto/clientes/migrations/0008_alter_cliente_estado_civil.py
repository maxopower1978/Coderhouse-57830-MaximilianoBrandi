# Generated by Django 5.1.1 on 2024-09-22 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_remove_cliente_contraseña1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado_civil',
            field=models.CharField(choices=[('', 'Seleccione'), ('SOLTERO', 'soltero'), ('CASADO', 'casado'), ('DIVORCIADO', 'divorciado'), ('SEPARADO', 'separado'), ('VIUDO', 'viudo'), ('CONCUBINO', 'concubino')], default='', max_length=20),
        ),
    ]
