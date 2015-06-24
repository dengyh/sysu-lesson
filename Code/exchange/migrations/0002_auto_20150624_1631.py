# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchange',
            name='state',
        ),
        migrations.AddField(
            model_name='exchange',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
