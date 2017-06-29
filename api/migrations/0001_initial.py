# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('header', models.IntegerField(default=0)),
                ('domainManager', models.IntegerField(default=0)),
                ('objectClass', models.IntegerField(default=0)),
                ('serialNumber', models.BigIntegerField(default=0)),
                ('location', models.IntegerField(default=0)),
                ('position', models.IntegerField(default=0)),
            ],
        ),
    ]
