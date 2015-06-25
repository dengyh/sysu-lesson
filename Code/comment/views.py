# -*- coding: utf8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Comment
from lesson.models import Lesson
import json

@login_required
@require_POST
def create_comment(request):
    result = False
    message = ''
    lessonId = int(request.POST.get('lesson'))
    try:
        lesson = Lesson.objects.get(id=lessonId)
    except:
        lesson = None
    if lesson:
        content = request.POST.get('content', None)
        if content:
            comment = Comment.objects.create(lesson=lesson,
                content=content, user=request.user, name=request.user.username)
            result = True
        else:
            message = '表单内容不全'
    else:
        message = '课程不存在'
    # return HttpResponse(json.dumps({
    #     'result': result,
    #     'message': message,
    #     }))
    return redirect('/lesson/' + str(lessonId) + '/')
