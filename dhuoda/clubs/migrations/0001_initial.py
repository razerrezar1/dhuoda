# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-21 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='club_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('contenu', models.TextField()),
                ('dateCreation', models.DateTimeField(default=django.utils.timezone.now)),
                ('datePublication', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='club_Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('dateCreation', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
