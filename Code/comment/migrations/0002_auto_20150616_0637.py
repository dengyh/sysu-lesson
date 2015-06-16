# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=b'Sysuer', max_length=64),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
