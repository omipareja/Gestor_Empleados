# Generated by Django 3.1.6 on 2021-02-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre Corto'),
        ),
    ]