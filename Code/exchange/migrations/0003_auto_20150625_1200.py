# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_auto_20150624_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
