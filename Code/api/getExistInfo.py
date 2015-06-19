# -*- coding: utf-8 -*-
import re

from sysu import Sysuer
from config import userId, password

import sys
sys.path.append('..')
from school.models import School
from lesson.models import Lesson

user = Sysuer(userId, password)
user.cookie = 'JSESSIONID=382DDF4BC1B9C489A2957581683C508B'

xnd = [
    '2006-2007', '2007-2008', '2008-2009', '2009-2010',
    '2010-2011', '2011-2012', '2012-2013', '2013-2014',
    '2014-2015',
]

def migrateSchoolToDatabase():
    schools = user.getAllSchools()
    pattern = re.compile(r'\{"[^\}]*"\}')
    results = pattern.finditer(schools)
    for item in results:
        oneSchool = item.group()
        namePattern = re.compile(r'(?<="yxsmc":")([^"]+?)(?=")')
        name = namePattern.search(oneSchool).group()
        print name
        engNamePattern = re.compile(r'(?<="yxsywmc":")([^"]+?)(?=")')
        try:
            engName = engNamePattern.search(oneSchool).group()
        except:
            engName = ''
        numberPattern = re.compile(r'(?<="yxsh":")([^"]+?)(?=")')
        number = numberPattern.search(oneSchool).group()
        schoolObj = School(name=name,
                englishName=engName, number=number)
        schoolObj.save();

def totalSchools():
    schools = user.getAllSchools()
    pattern = re.compile(r'\{"[^\}]*"\}')
    results = pattern.finditer(schools)
    schools = [i.group() for i in results]
    return schools

def migrateOneLesson(oneLesson):
    lessonIdPattern = re.compile(r'(?<="kch":")([^"]+?)(?=")')
    lessonId = lessonIdPattern.search(oneLesson).group()
    schoolPattern = re.compile(r'(?<="kkdw":")([^"]+?)(?=")')
    try:
        schoolNumber = schoolPattern.search(oneLesson).group()
    except:
        schoolNumber = lessonId[:5]
    try:
        schoolObj = School.objects.get(number=schoolNumber)
    except:
        schoolObj = School.objects.get(number='69000')

    titlePattern = re.compile(r'(?<="kcmc":")([^"]+?)(?=")')
    title = titlePattern.search(oneLesson).group()
    descPattern = re.compile(r'(?<="xddx":")([^"]+?)(?=")')
    try:
        description = descPattern.search(oneLesson).group()
    except:
        description = ''
    classHourPattern = re.compile(r'(?<="xs":")([^"]+?)(?=")')
    try:
        classHour = classHourPattern.search(oneLesson).group()
    except:
        classHour = 'None'
    creditPattern = re.compile(r'(?<="xf":")([^"]+?)(?=")')
    try:
        credit = creditPattern.search(oneLesson).group()
    except:
        credit = 'None'
    campusPattern = re.compile(r'(?<="skjsszxq":")([^"]+?)(?=")')
    try:
        campus = campusPattern.search(oneLesson).group()
    except:
        campus = ''
    teacherPattern = re.compile(r'(?<="zjjsxm":")([^"]+?)(?=")')
    try:
        teacher = teacherPattern.search(oneLesson).group()[:128]
    except:
        teacher = ''
    if '__' in teacher:
        teacher = ''
    print teacher
    teachTypePattern = re.compile(r'(?<="pylb":")([^"]+?)(?=")')
    try:
        teachType = teachTypePattern.search(oneLesson).group()
    except:
        teachType = '01'
    typePattern = re.compile(r'(?<="kclb":")([^"]+?)(?=")')
    type = typePattern.search(oneLesson).group()
    try:
        lessonObj = Lesson.objects.get(lessonId=lessonId, teacher=teacher)
    except Lesson.DoesNotExist:
        try:
            lessonObj = Lesson.objects.create(school=schoolObj,
                        lessonId=lessonId,
                        title=title,
                        description=description,
                        classHour=classHour,
                        credit=credit,
                        campus=campus,
                        teacher=teacher,
                        teachType=teachType,
                        type=type)
        except:
            pass


def migrateLessonToDatabase():
    for year in xnd:
        lessons = user.getCourses(xnd=year)
        print lessons
        pattern = re.compile(r'\{"[^\}]*"\}')
        results = pattern.finditer(lessons)
        for item in results:
            oneLesson = item.group()
            migrateOneLesson(oneLesson)
