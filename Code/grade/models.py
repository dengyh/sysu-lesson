# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from lesson.models import Lesson

# Create your models here.

class Grade(models.Model):
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson)
    year = models.IntegerField()
    term = models.IntegerField(choices = (
        (0, u'上学期'),
        (1, u'下学期'),
        (2, u'小学期')
    ))
    score = models.IntegerField()
    ranking = models.IntegerField()
    total = models.IntegerField()

    def __unicode__(self):
        return self.user.first_name + '\'s get ' + \
            str(self.score) + ' in lesson ' + str(self.lesson.id)

    class Meta:
        ordering = ['year', 'term', 'user']
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
