# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('origem', models.CharField(max_length=10, verbose_name='Origem')),
                ('destino', models.CharField(max_length=10, verbose_name='Destino')),
                ('distancia', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'ordering': ('-created',),
            },
        ),
    ]