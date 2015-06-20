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
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('time', models.DateTimeField()),
                ('name', models.CharField(default=b'Sysuer', max_length=64)),
                ('follow', models.ForeignKey(blank=True, to='comment.Comment', null=True)),
                ('lesson', models.ForeignKey(to='lesson.Lesson')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['lesson', 'time', 'user'],
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
