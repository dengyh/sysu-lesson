# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lessonIn', models.CharField(max_length=128, null=True, blank=True)),
                ('lessonOut', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
                ('deadline', models.DateTimeField(null=True, blank=True)),
                ('time', models.DateTimeField(verbose_name=b'published time')),
                ('state', models.CharField(default=b'i', max_length=4, choices=[(b'i', b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (b'c', b'\xe5\xb7\xb2\xe6\x92\xa4\xe9\x94\x80'), (b'f', b'\xe5\xb7\xb2\xe7\xbb\x93\xe6\x9d\x9f')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
                'verbose_name': 'Exchanges',
            },
        ),
    ]
