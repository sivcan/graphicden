# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_user_upload_csv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Upload_CSV_File',
            field=models.FileField(upload_to='/media/'),
        ),
    ]
