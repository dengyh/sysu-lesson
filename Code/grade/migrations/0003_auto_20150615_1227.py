# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_auto_20150615_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='ranking',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='total',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
