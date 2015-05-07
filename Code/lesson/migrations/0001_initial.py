# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(null=True, blank=True)),
                ('campus', models.CharField(max_length=16, choices=[(b'east', '\u4e1c\u6821\u533a'), (b'north', '\u5317\u6821\u533a'), (b'south', '\u5357\u6821\u533a'), (b'zhuhai', '\u73e0\u6d77\u6821\u533a')])),
                ('teacher', models.CharField(max_length=32, null=True, blank=True)),
                ('teachType', models.CharField(max_length=4, choices=[(b'01', '\u4e3b\u4fee'), (b'02', '\u8f85\u4fee')])),
                ('type', models.CharField(max_length=4, choices=[(b'01', '\u516c\u5fc5'), (b'02', '\u4e13\u5fc5'), (b'03', '\u516c\u9009'), (b'04', '\u4e13\u9009')])),
                ('evaluationValue', models.IntegerField(default=0)),
                ('evaluationCount', models.IntegerField(default=0)),
                ('school', models.ForeignKey(to='school.School')),
            ],
            options={
                'ordering': ['campus'],
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
    ]
