from __future__ import unicode_literals

from django.db import models


class TableOne(models.Model):
    name = models.CharField(max_length=100)

    auto_create_schema = True


class TableTwo(models.Model):
    name = models.CharField(max_length=100)
    table_one = models.ForeignKey(TableOne, on_delete=models.CASCADE)

    auto_create_schema = True
