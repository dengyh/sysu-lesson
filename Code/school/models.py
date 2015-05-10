# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    englishName = models.CharField(max_length = 64, null = True, blank = True)
    number = models.CharField(max_length = 128, unique = True)
    campus = models.CharField(max_length = 16, choices = (
        ('east', u'东校区'),
        ('north', u'北校区'),
        ('south', u'南校区'),
        ('zhuhai', u'珠海校区')
    ), null = True, blank = True)
    dean = models.CharField(max_length = 16, null = True, blank = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

class Department(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    englishName = models.CharField(max_length = 64, null = True, blank = True)
    number = models.CharField(max_length = 128, unique = True)
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

class Major(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    englishName = models.CharField(max_length = 64, null = True, blank = True)
    number = models.CharField(max_length = 128, unique = True)
    department = models.ForeignKey(Department)
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Major'
        verbose_name_plural = 'Majors'
