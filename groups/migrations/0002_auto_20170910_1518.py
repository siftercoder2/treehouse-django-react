# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 20:18
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name'),
        ),
        migrations.AddField(
            model_name='family',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name'),
        ),
    ]