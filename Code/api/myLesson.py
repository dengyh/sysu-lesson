# -*- coding: utf-8 -*-

from school.models import School

type = {
    '10': u'公必',
    '11': u'专必',
    '30': u'公选',
    '21': u'专选'
}

class MyLesson:
    def __init__(self, year, term, teacher,
            teachType, lessonType, lessonId,
            credit, school, name, time):
        self.year = year
        self.term = term
        self.teacher = teacher
        if teachType == '01':
            self.teachType = u'主修'
        else:
            self.teachType = u'辅修'
        self.lessonType = type[lessonType]
        self.lessonId = lessonId
        self.credit = credit
        self.school = school
        self.name = name
        self.time = time

    def get_school_name(self):
        school = School.objects.get(number=self.school)
        return school.name

    def __str__(self):
        return name
