# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChianDoWebsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ChianDoWebsite.Blog'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ChianDoWebsite.Blog'),
        ),
        migrations.AlterField(
            model_name='gallerypicture',
            name='picture',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ChianDoWebsite.Picture'),
        ),
    ]
