# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enunciado', '0003_auto_20171121_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestion_grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enunciado.Grado')),
                ('materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enunciado.Materia')),
            ],
        ),
    ]