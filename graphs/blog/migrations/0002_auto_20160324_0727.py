# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type_graph',
        ),
        migrations.AddField(
            model_name='user',
            name='type_Of_Graph',
            field=models.CharField(choices=[('Bar', 'BarGraph'), ('Line', 'LineGraph')], default=1, max_length=10),
        ),
    ]
