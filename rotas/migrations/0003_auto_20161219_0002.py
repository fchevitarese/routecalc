# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotas', '0002_rota_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rota',
            name='distancia',
            field=models.IntegerField(verbose_name='Distância'),
        ),
    ]
