# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='classHour',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='credit',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='lessonId',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='campus',
            field=models.CharField(blank=True, max_length=16, null=True, choices=[(b'4', '\u4e1c\u6821\u533a'), (b'north', '\u5317\u6821\u533a'), (b'south', '\u5357\u6821\u533a'), (b'zhuhai', '\u73e0\u6d77\u6821\u533a')]),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='type',
            field=models.CharField(max_length=4, choices=[(b'10', '\u516c\u5fc5'), (b'11', '\u4e13\u5fc5'), (b'03', '\u516c\u9009'), (b'21', '\u4e13\u9009')]),
        ),
    ]
