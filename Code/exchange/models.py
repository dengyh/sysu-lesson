# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from lesson.models import Lesson

# Create your models here.

class Exchange(models.Model):
    user = models.ForeignKey(User)
    lessonIn = models.CharField(max_length=128, blank=True, null=True)
    lessonOut = models.CharField(max_length=128)
    phone = models.CharField(max_length = 16)
    email = models.EmailField(max_length = 64)
    description = models.TextField(null = True, blank = True)
    deadline = models.DateTimeField(null = True, blank = True)
    time = models.DateTimeField('published time')
    finished = models.BooleanField(default=False)

    def finish(self):
        self.finished = True

    def get_state(self):
        if self.finished:
            return '已完成'
        else:
            return '进行中'

    def __unicode__(self):
        try:
            return 'Exchange hold by ' + self.user + \
                ' for lesson ' + str(self.lesson.id)
        except:
            return 'An Exchange'

    class Meta:
        ordering = ['-time']
        verbose_name = 'Exchange'
        verbose_name = 'Exchanges'
