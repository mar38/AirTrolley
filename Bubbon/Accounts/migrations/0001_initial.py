# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-01 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('First_Name', models.CharField(default=b'Null', max_length=16)),
                ('Last_Name', models.CharField(default=b'Null', max_length=16)),
                ('username', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
                ('Address', models.CharField(max_length=16)),
                ('PostCode', models.CharField(default=b'Null', max_length=16)),
                ('Contact', models.CharField(default=b'Null', max_length=10)),
            ],
        ),
    ]
