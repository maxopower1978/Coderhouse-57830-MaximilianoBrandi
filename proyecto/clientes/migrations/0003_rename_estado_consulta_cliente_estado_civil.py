# Generated by Django 5.1.1 on 2024-09-21 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_avatar_alter_cliente_direccion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='estado_consulta',
            new_name='estado_civil',
        ),
    ]
