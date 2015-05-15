# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_auto_20150513_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
