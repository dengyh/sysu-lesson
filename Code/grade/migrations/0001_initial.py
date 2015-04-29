# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('term', models.IntegerField(choices=[(0, '\u4e0a\u5b66\u671f'), (1, '\u4e0b\u5b66\u671f'), (2, '\u5c0f\u5b66\u671f')])),
                ('score', models.IntegerField()),
                ('ranking', models.IntegerField()),
                ('total', models.IntegerField()),
                ('lesson', models.ForeignKey(to='lesson.Lesson')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['year', 'term', 'user'],
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
            },
        ),
    ]
