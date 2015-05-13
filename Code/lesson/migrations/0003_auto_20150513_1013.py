# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_auto_20150513_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='campus',
            field=models.CharField(blank=True, max_length=16, null=True, choices=[(b'4', '\u4e1c\u6821\u533a'), (b'2', '\u5317\u6821\u533a'), (b'3', '\u5357\u6821\u533a'), (b'1', '\u73e0\u6d77\u6821\u533a')]),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='type',
            field=models.CharField(max_length=4, choices=[(b'10', '\u516c\u5fc5'), (b'11', '\u4e13\u5fc5'), (b'30', '\u516c\u9009'), (b'21', '\u4e13\u9009')]),
        ),
    ]
