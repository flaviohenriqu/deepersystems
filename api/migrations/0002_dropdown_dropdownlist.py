# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dropdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DropdownList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('dropdown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dropdown_values', to='api.Dropdown')),
            ],
        ),
    ]
