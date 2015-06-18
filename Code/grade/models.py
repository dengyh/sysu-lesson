# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from lesson.models import Lesson

# Create your models here.

class Grade(models.Model):
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson)
    year = models.CharField(max_length=128)
    term = models.CharField(choices = (
        ('2', u'上学期'),
        ('3', u'下学期'),
        ('1', u'小学期'),
        ('4', u'未知')
    ), max_length='16')
    score = models.IntegerField()
    ranking = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.user.first_name + '\'s get ' + \
            str(self.score) + ' in lesson ' + str(self.lesson.id)

    class Meta:
        ordering = ['year', 'term', 'user']
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        unique_together = ('user', 'lesson',)
