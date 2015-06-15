# -*- coding: utf-8 -*-
import re

from sysu import Sysuer
from config import userId, password

import sys
sys.path.append('..')
from school.models import School
from lesson.models import Lesson

user = Sysuer(userId, password)
user.cookie = 'JSESSIONID=135792A197F235DEB7170E8976AE50C9'

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
        namePattern = re.compile(r'"yxsmc":"[^"]+"')
        name = namePattern.search(oneSchool).group()[9:-1]
        print name
        engNamePattern = re.compile(r'"yxsywmc":"[^"]+"')
        try:
            engName = engNamePattern.search(oneSchool).group()[11:-1]
        except:
            engName = ''
        numberPattern = re.compile(r'"yxsh":"[^"]+"')
        number = numberPattern.search(oneSchool).group()[8:-1]
        schoolObj = School(name=name,
                englishName=engName, number=number)
        schoolObj.save();

def migrateOneLesson(oneLesson):
    lessonIdPattern = re.compile(r'"kch":"[^"]+"')
    lessonId = lessonIdPattern.search(oneLesson).group()[7:-1]
    schoolPattern = re.compile(r'"kkdw":"[^"]+"')
    try:
        schoolNumber = schoolPattern.search(oneLesson).group()[8:-1]
    except:
        schoolNumber = lessonId[:5]
    try:
        schoolObj = School.objects.get(number=schoolNumber)
    except:
        schoolObj = School.objects.get(number='69000')

    titlePattern = re.compile(r'"kcmc":"[^"]+"')
    title = titlePattern.search(oneLesson).group()[8:-1]
    descPattern = re.compile(r'"xddx":"[^"]+"')
    try:
        description = descPattern.search(oneLesson).group()[8:-1]
    except:
        description = ''
    classHourPattern = re.compile(r'"xs":"[^"]+"')
    try:
        classHour = classHourPattern.search(oneLesson).group()[6:-1]
    except:
        classHour = '0'
    creditPattern = re.compile(r'"xf":"[^"]+"')
    try:
        credit = creditPattern.search(oneLesson).group()[6:-1]
    except:
        credit = '0'
    campusPattern = re.compile(r'"skjsszxq":"[^"]+"')
    try:
        campus = campusPattern.search(oneLesson).group()[12:-1]
    except:
        campus = ''
    teacherPattern = re.compile(r'"zjjsxm":"[^"]+"')
    try:
        teacher = teacherPattern.search(oneLesson).group()[10:-1]
    except:
        teacher = ''
    teachTypePattern = re.compile(r'"pylb":"[^"]+"')
    try:
        teachType = teachTypePattern.search(oneLesson).group()[8:-1]
    except:
        teachType = '01'
    typePattern = re.compile(r'"kclb":"[^"]+"')
    type = typePattern.search(oneLesson).group()[8:-1]
    try:
        lessonObj = Lesson(school=schoolObj,
                        lessonId=lessonId,
                        title=title,
                        description=description,
                        classHour=classHour,
                        credit=credit,
                        campus=campus,
                        teacher=teacher[:128],
                        teachType=teachType,
                        type=type)
        lessonObj.save()
        return lessonObj
    except:
        pass


def migrateLessonToDatabase():
    for year in xnd:
        lessons = user.getCourses(xnd=year)
        pattern = re.compile(r'\{"[^\}]*"\}')
        results = pattern.finditer(lessons)
        for item in results:
            oneLesson = item.group()
            migrateOneLesson(oneLesson)
