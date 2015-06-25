# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meterial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterial',
            name='term',
            field=models.IntegerField(blank=True, null=True, choices=[(0, '\u4e0a\u5b66\u671f'), (1, '\u4e0b\u5b66\u671f'), (2, '\u5c0f\u5b66\u671f')]),
        ),
        migrations.AlterField(
            model_name='meterial',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='meterial',
            name='year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
