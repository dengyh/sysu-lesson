# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='term',
            field=models.CharField(max_length=b'16', choices=[(b'2', '\u4e0a\u5b66\u671f'), (b'3', '\u4e0b\u5b66\u671f'), (b'1', '\u5c0f\u5b66\u671f'), (b'4', '\u672a\u77e5')]),
        ),
    ]
