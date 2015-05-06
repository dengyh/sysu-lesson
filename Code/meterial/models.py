# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from lesson.models import Lesson

# Create your models here.

class Meterial(models.Model):
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson)
    year = models.IntegerField()
    term = models.IntegerField(choices = (
        (0, u'上学期'),
        (1, u'下学期'),
        (2, u'小学期')
    ))
    file = models.FileField(max_length = 256)
    title = models.CharField(max_length = 256)
    remark = models.CharField(max_length = 256, null = True, blank = True)
    favour = models.IntegerField(default = 0)
    time = models.IntegerField()

    def __unicode__(self):
        return 'Meterial for lesson ' + str(self.lesson.id)

    class Meta:
        ordering = ['lesson', 'time']
        verbose_name = 'Meterial'
        verbose_name_plural = 'Meterials'
