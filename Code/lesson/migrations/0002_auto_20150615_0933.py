# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set([('lessonId', 'teacher')]),
        ),
    ]
