# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='lessonIn',
            field=models.ForeignKey(related_name='lesson_in', blank=True, to='lesson.Lesson', null=True),
        ),
        migrations.AddField(
            model_name='exchange',
            name='lessonOut',
            field=models.ForeignKey(related_name='lesson_out', to='lesson.Lesson'),
        ),
        migrations.AddField(
            model_name='exchange',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
