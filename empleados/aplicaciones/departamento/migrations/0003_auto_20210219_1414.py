# Generated by Django 3.1.6 on 2021-02-19 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20210218_0125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi departamento', 'verbose_name_plural': 'Mis departamentos'},
        ),
    ]
