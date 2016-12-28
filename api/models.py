from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    job_position = models.CharField(max_length=100)
    email = models.EmailField()
    hours_per_week = models.IntegerField()
    where_found_us = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    english_level = models.CharField(max_length=20)
    comments = models.TextField()


class Dropdown(models.Model):
    field_name = models.CharField(max_length=100)


class DropdownList(models.Model):
    text = models.CharField(max_length=100)
    dropdown = models.ForeignKey(Dropdown,
            related_name='dropdown_values',
            on_delete=models.CASCADE)

