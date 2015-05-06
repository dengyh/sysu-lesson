# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class School(models.Model):
    """ The class 'School' indicate the school of sysu """
    id = models.IntegerField(primary_key=True) # the id of school
    chineseName = models.CharField(max_length=128)
    englishName = models.CharField(max_length=128)

    def __unicode__(self):
        return self.chineseName

    class Meta:
        ordering = ['id']
        verbose_name = 'School'
        cerbose_name = 'schools'
