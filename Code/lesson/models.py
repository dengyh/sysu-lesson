# -*- coding: utf-8 -*-
from django.db import models

from school.models import School
# Create your models here.

class Lesson(models.Model):
    school = models.ForeignKey(School)
    lessonId = models.CharField(max_length = 32)
    title = models.CharField(max_length = 128)
    description = models.TextField(null = True, blank = True)
    classHour = models.CharField(max_length = 16)
    credit = models.CharField(max_length = 8)
    campus = models.CharField(max_length = 16, choices = (
        ('4', u'东校区'),
        ('2', u'北校区'),
        ('3', u'南校区'),
        ('1', u'珠海校区')
    ), null = True, blank = True)
    teacher = models.CharField(max_length=128, null = True, blank = True) #老外的名字太长了
    teachType = models.CharField(max_length = 4, choices = (
        ('01', u'主修'),
        ('02', u'辅修'),  #unkonw
        # todo 
    ))
    type = models.CharField(max_length = 4, choices = (
        ('10', u'公必'),
        ('11', u'专必'),
        ('30', u'公选'),
        ('21', u'专选'),
    ))
    evaluationValue = models.IntegerField(default = 0)
    evaluationCount = models.IntegerField(default = 0)
    gradeNumber = models.IntegerField(default = 0)

    def add_grade_number(self):
        self.gradeNumber += 1

    def get_evaluation(self):
        try:
            return self.evaluationValue/self.evaluationCount
        except:
            return 0

    def __unicode__(self):
        return self.title

    def add_evaluation(self, value):
        self.evaluationValue += value
        self.evaluationCount += 1

    class Meta:
        ordering = ['-evaluationCount', '-gradeNumber', 'title']
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        unique_together = ('lessonId', 'teacher', )

