# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enunciado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enunciado.Profesor'),
        ),
    ]
