# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 23:00
from __future__ import unicode_literals

from django.db import migrations


def load_dropdown_values(apps, schema_editor):
    Dropdown = apps.get_model("api", "Dropdown")
    dropdown_job = Dropdown(field_name="job_position")
    dropdown_job.save()
    dropdown_where = Dropdown(field_name="where_found_us")
    dropdown_where.save()
    dropdown_country = Dropdown(field_name="country")
    dropdown_country.save()
    dropdown_country.dropdown_values.create(text="USA")
    dropdown_country.dropdown_values.create(text="Brazil")
    dropdown_country.dropdown_values.create(text="China")
    dropdown_country.dropdown_values.create(text="Romania")
    dropdown_country.dropdown_values.create(text="Ukraine")
    dropdown_english = Dropdown(field_name="english_level")
    dropdown_english.save()
    dropdown_english.dropdown_values.create(text="Good")
    dropdown_english.dropdown_values.create(text="OK")
    dropdown_english.dropdown_values.create(text="Bad")

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_dropdown_dropdownlist'),
    ]

    operations = [
            migrations.RunPython(load_dropdown_values),
    ]
