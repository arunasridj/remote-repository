# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-10 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdata',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
