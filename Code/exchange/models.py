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
    state = models.CharField(max_length=4, choices = (
        ('i', '进行中'),
        ('c', '已撤销'),
        ('f', '已结束'),
    ), default = 'i')

    def get_state(self):
        return self.state

    def finish(self):
        if self.state == 'i':
            self.state = 'f'

    def cancel(self):
        if self.state == 'i':
            self.state = 'c'

    def __unicode__(self):
        try:
            return 'Exchange hold by ' + self.first_name + \
                ' for lesson ' + str(self.lesson.id)
        except:
            return 'An Exchange'

    class Meta:
        ordering = ['-time']
        verbose_name = 'Exchange'
        verbose_name = 'Exchanges'
