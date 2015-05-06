# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from lesson.models import Lesson

# Create your models here.

class Exchange(models.Model):
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson)
    phone = models.CharField(max_length = 16)
    email = models.EmailField(max_length = 64)
    time = models.IntegerField()
    finish = models.BooleanField(default = False)
    active = models.BooleanField(default = True)

    def __unicode__(self):
        return 'Exchange hold by ' + self.first_name + \
            ' for lesson ' + str(self.lesson.id)

    class Meta:
        ordering = ['year', 'term', 'time']
        verbose_name = 'Exchange'
        verbose_name = 'Exchanges'
