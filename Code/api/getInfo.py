# -*- coding: utf-8 -*-
from sysu import Sysuer
from myLesson import MyLesson

import re
import sys
sys.path.append('..')
from lesson.models import Lesson
from django.contrib.auth.models import User
from grade.models import Grade
from school.models import School
from lesson.models import Lesson

def getGrades(user, jwxt_user):
    gradesStr = jwxt_user.getScore()
    pattern = pattern = re.compile(r'\{"[^\}]*"\}')
    results = pattern.finditer(gradesStr)
    for item in results:
        grade = item.group()
        try:
            lessonIdPattern = re.compile(r'(?<="kch":")([^"]+?)(?=")')
            lessonId = lessonIdPattern.search(grade).group()
            teacherPattern = re.compile(r'(?<="jsxm":")([^"]+?)(?=")')
            try:
                teacher = teacherPattern.search(grade).group()
            except:
                teacher = ''
            lesson = Lesson.objects.get(lessonId=lessonId, teacher=teacher)
        except Lesson.DoesNotExist:
            schoolNumber = lessonId[:5]
            try:
                schoolObj = School.objects.get(number=schoolNumber)
            except:
                schoolObj = School.objects.get(number='69000')
            titlePattern = re.compile(r'(?<="kcmc":")([^"]+?)(?=")')
            title = titlePattern.search(grade).group()
            classHour = 'None'
            creditPattern = re.compile(r'(?<="xf":")([^"]+?)(?=")')
            try:
                credit = creditPattern.search(grade).group()
            except:
                credit = '0'
            campus = ''
            teachType = '01'
            typePattern = re.compile(r'(?<="kclb":")([^"]+?)(?=")')
            type = typePattern.search(grade).group()
            lesson = Lesson(school=schoolObj,
                        lessonId=lessonId,
                        title=title,
                        description='',
                        classHour=classHour,
                        credit=credit,
                        campus=campus,
                        teacher=teacher[:128],
                        teachType=teachType,
                        type=type
             )
            lesson.save()
        yearPattern = re.compile(r'(?<="xnd":")([^"]+?)(?=")')
        try:
            year = yearPattern.search(grade).group()
        except:
            year = 'unknow'
        scorePattern = re.compile(r'(?<="zzcj":")([^"]+?)(?=")')
        try:
            score = int(scorePattern.search(grade).group())
        except:
            continue
        rankPattern = re.compile(r'(?<="jxbpm":")([^"]+?)(?=")')
        try:
            rank = rankPattern.search(grade).group()
        except:
            ranking = int
            total = int
        else:
            rank_list = map(int, re.findall(r'\d+', rank))
            try:
                ranking = rank_list[0]
                total = rank_list[1]
            except:
                ranking = int
                total = int
        termPattern = re.compile(r'(?<="xq":")([^"]+?)(?=")')
        try:
            term = termPattern.search(grade).group()
        except:
            term = '4'
        try:
            gradeObj = Grade.objects.get(user=user, lesson=lesson)
        except Grade.DoesNotExist:
            gradeObj = Grade(
                    user=user,
                    lesson=lesson,
                    year=year,
                    term=term,
                    score=score,
                    ranking=ranking,
                    total=total
            )
            gradeObj.save()
            lesson.add_grade_number()
            lesson.save()

def getSelectResults(user, sysuer):
    select_results = []
    resultsStr = sysuer.getResultOfCourseSelection()
    pattern = pattern = re.compile(r'\{"[^\}]*"\}')
    results = pattern.finditer(resultsStr)
    for item in results:
        result = item.group()
        yearPattern = re.compile(r'(?<="xnd":")([^"]+?)(?=")')
        year = yearPattern.search(result).group()
        termPattern = re.compile(r'(?<="xq":")([^"]+?)(?=")')
        term = termPattern.search(result).group()
        teacherPattern = re.compile(r'(?<="xm":")([^"]+?)(?=")')
        try:
            teacher = teacherPattern.search(result).group()
        except:
            teacher = u'无教师信息'
        teachTypePattern = re.compile(r'(?<="pylbm":")([^"]+?)(?=")')
        teachType = teachTypePattern.search(result).group()
        lessonTypePattern = re.compile(r'(?<="kclbm":")([^"]+?)(?=")')
        lessonType = lessonTypePattern.search(result).group()
        lessonIdPattern = re.compile(r'(?<="kch":")([^"]+?)(?=")')
        lessonId = lessonIdPattern.search(result).group()
        creditPattern = re.compile(r'(?<="xf":")([^"]+?)(?=")')
        credit = creditPattern.search(result).group()
        schoolPattern = re.compile(r'(?<="kkdw":")([^"]+?)(?=")')
        school = schoolPattern.search(result).group()
        namePattern = re.compile(r'(?<="kcmc":")([^"]+?)(?=")')
        name = namePattern.search(result).group()
        timePattern = re.compile(r'(?<="sksjdd":")([^"]+?)(?=")')
        try:
            time = timePattern.search(result).group()
        except:
            time = u'无上课时间和地点信息'
        my_lesson = MyLesson(year=year,
                term=term, teacher=teacher,
                teachType=teachType, lessonType=lessonType,
                lessonId=lessonId, credit=credit, school=school,
                name=name, time=time)
        select_results.append(my_lesson)
    return select_results

def getGradePoint(sysuer):
    """ 获取绩点 """
    gradePointStr = sysuer.getGrade()
    grade_point = {}
    pattern = pattern = re.compile(r'\{"[^\}]*"\}')
    results = pattern.finditer(gradePointStr)
    for item in results:
        gradePoint = item.group()
        colOnePattern = re.compile(r'(?<="oneColumn":")([^"]+?)(?=")')
        colOne = colOnePattern.search(gradePoint).group()
        colTwoPattern = re.compile(r'(?<="twoColumn":")([^"]+?)(?=")')
        colTwo = colTwoPattern.search(gradePoint).group()
        grade_point[colOne] = colTwo
    return grade_point

def getCredit(sysuer):
    """ 获取学分 """
    creditStr = sysuer.getCredit()
    credits = {}
    pattern = pattern = re.compile(r'\{"[^\}]*"\}')
    results = pattern.finditer(creditStr)
    for item in results:
        gradePoint = item.group()
        colOnePattern = re.compile(r'(?<="oneColumn":")([^"]+?)(?=")')
        colOne = colOnePattern.search(gradePoint).group()
        colTwoPattern = re.compile(r'(?<="twoColumn":")([^"]+?)(?=")')
        colTwo = colTwoPattern.search(gradePoint).group()
        credits[colOne] = colTwo
    return credits
