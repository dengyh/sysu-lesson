# -*- coding: utf-8 -*-
from django.db import models

from school.models import School
# Create your models here.

class Lesson(models.Model):
    school = models.ForeignKey(School)
    title = models.CharField(max_length = 128)
    description = models.TextField(null = True, blank = True)
    campus = models.CharField(max_length = 16, choices = (
        ('east', u'东校区'),
        ('north', u'北校区'),
        ('south', u'南校区'),
        ('zhuhai', u'珠海校区')
    ))
    teacher = models.CharField(max_length = 32, null = True, blank = True)
    teachType = models.CharField(max_length = 4, choices = (
        ('01', u'主修'),
        ('02', u'辅修'),
        # todo 
    ))
    type = models.CharField(max_length = 4, choices = (
        ('01', u'公必'),
        ('02', u'专必'),
        ('03', u'公选'),
        ('04', u'专选'),
    ))
    evaluationValue = models.IntegerField(default = 0)
    evaluationCount = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.title

    def add_evaluation(self, value):
        self.evaluationValue += value
        self.evaluationCount += 1

    class Meta:
        ordering = ['campus']
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
