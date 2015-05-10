# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=64)),
                ('deadline', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField()),
                ('finish', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['time'],
                'verbose_name': 'Exchanges',
            },
        ),
    ]
