# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from lesson.models import Lesson

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson)
    content = models.TextField(null = True, blank = True)
    time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64, default='Sysuer')
    follow = models.ForeignKey('self', null = True, blank = True)

    def __unicode__(self):
        return 'Comment for lesson ' + str(self.lesson.id) + \
            ' from ' + self.user.first_name

    class Meta:
        ordering = ['lesson', 'time', 'user']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
