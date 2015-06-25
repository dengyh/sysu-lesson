# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from meterial.models import Meterial
from meterial.forms import MeterialForm
from lesson.models import Lesson

import json

@require_POST
@login_required
def create_meterial(request):
    result = False
    message = ''
    lessonId = int(request.POST.get('lesson'))
    try:
        lesson = Lesson.objects.get(id=lessonId)
    except:
        lesson = None
    if lesson:
        form = MeterialForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']
            meterial = Meterial.objects.create(title=title, file=file,
                lesson=lesson, user=request.user)
            result = True
            message = 'Succeed'
        else:
            message = '资料不全'
            print form.errors
    else:
        message = '课程不存在'

    return redirect('/lesson/' + str(lessonId) + '/')