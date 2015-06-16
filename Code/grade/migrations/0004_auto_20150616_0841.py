# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0003_auto_20150615_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='term',
            field=models.IntegerField(choices=[(1, '\u4e0a\u5b66\u671f'), (2, '\u4e0b\u5b66\u671f'), (3, '\u5c0f\u5b66\u671f'), (4, '\u672a\u77e5')]),
        ),
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together=set([('user', 'lesson')]),
        ),
    ]
