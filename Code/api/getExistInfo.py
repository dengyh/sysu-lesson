# -*- coding: utf-8 -*-
import re

from sysu import Sysuer
from config import userId, password

import sys
sys.path.append('..')
from school.models import School
from lesson.models import Lesson

def migrateSchoolToDatabase():
    user = Sysuer(userId, password)
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

def migrateLessonToDatabase():
    user = Sysuer(userId, password)
    lessons = user.getCourses()
    pattern = re.compile(r'\{"[^\}]*"\}')
    results = pattern.finditer(lessons)
    for item in results:
        oneLesson = item.group()
        schoolPattern = re.compile(r'"kkdw":"[^"]+"')
        schoolNumber = schoolPattern.search(oneLesson).group()[8:-1]
        try:
            schoolObj = School.objects.get(number=schoolNumber)
        except:
            schoolObj = School.objects.get(number='69000')
        lessonIdPattern = re.compile(r'"kch":"[^"]+"')
        lessonId = lessonIdPattern.search(oneLesson).group()[7:-1]
        titlePattern = re.compile(r'"kcmc":"[^"]+"')
        title = titlePattern.search(oneLesson).group()[8:-1]
        descPattern = re.compile(r'"xddx":"[^"]+"')
        try:
            description = descPattern.search(oneLesson).group()[8:-1]
        except:
            description = ''
        classHourPattern = re.compile(r'"xs":"[^"]+"')
        classHour = classHourPattern.search(oneLesson).group()[6:-1]
        creditPattern = re.compile(r'"xf":"[^"]+"')
        credit = creditPattern.search(oneLesson).group()[6:-1]
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
        teachType = teachTypePattern.search(oneLesson).group()[8:-1]
        typePattern = re.compile(r'"kclb":"[^"]+"')
        type = typePattern.search(oneLesson).group()[8:-1]
        lessonObj = Lesson(school=schoolObj,
                lessonId=lessonId,
                title=title,
                description=description,
                classHour=classHour,
                credit=credit,
                campus=campus,
                teacher=teacher,
                teachType=teachType,
                type=type)
        lessonObj.save()



