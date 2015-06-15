from sysu import Sysuer

from .getExistInfo import migrateOneLesson
import re
import sys
sys.path.append('..')
from lesson.models import Lesson
from django.contrib.auth.models import User
from grade.models import Grade

def getGrades(jwxt_user, user):
    gradesStr = jwxt_user.getScore()
    pattern = pattern = re.compile(r'\{"[^\}]*"\}')
    results = pattern.finditer(gradesStr)
    for item in results:
        grade = item.group()
        lessonIdPattern = re.compile(r'"kch":"[^"]+"')
        try:
            lessonId = lessonIdPattern.search(grade).group()[7:-1]
        except:
            lesson = migrateOneLesson(grade)
        else:
            teacherPattern = re.compile(r'"jsxm":"[^"]+"')
            try:
                teacher = teacherPattern.search(grade).group()[8:-1]
            except:
                teacher = ''
            lessons = Lesson.objects.filter(lessonId=lessonId).filter(
                    teacher=teacher)
            try:
                lesson = lessons[0]
            except:
                lesson = migrateOneLesson(grade)
        yearPattern = re.compile(r'"xnd":"[^"]+"')
        try:
            year = yearPattern.search(grade).group()[7:-1]
        except:
            year = 'unknow'
        scorePattern = re.compile(r'"zzcj":"[^"]+"')
        try:
            score = scorePattern.search(grade).group()[8:-1]
        except:
            continue
        rankPattern = re.compile(r'"jxbpm":"[^"]+"')
        try:
            rank = rankPattern.search(grade).group()[9:-1]
        except:
            continue
        else:
            rank_list = map(int, re.findall(r'\d+', rank))
            try:
                ranking = rank_list[0]
                total = rank_list[1]
            except:
                ranking = None
                total = None
        termPattern = re.compile(r'"xq":"[^"]+"')
        try:
            termStr = termPattern.search(grade).group()[6:-1]
            term = int(termStr)
        except:
            term = 4
        try:
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
        except:
            pass
