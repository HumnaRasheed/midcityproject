# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-22 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_activity', '0003_event_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_num',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
