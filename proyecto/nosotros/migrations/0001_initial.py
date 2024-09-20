# Generated by Django 5.1.1 on 2024-09-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('matricula', models.TextField()),
                ('celular', models.IntegerField()),
                ('disponible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Nosotro',
                'verbose_name_plural': 'Nosotros',
            },
        ),
    ]
