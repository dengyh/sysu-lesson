# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST

# Create your views here.

from api.sysu import Sysuer
from api.parser import parseResultOfCourseSelection, parseScore

@require_GET
@login_required
def get_personal_grade(request):
    year = request.GET.get('year', '2014-2015')
    term = request.GET.get('term', '3')
    type = request.GET.get('type', '01')
    terms = ['', '小学期', '第二学期', '第三学期']
    current = {'year':year, 'term':terms[int(term)], 'type':type, 'termValue': term}
    user = Sysuer(username=request.user.username,
        cookie=request.session['cookie'])
    try:
        data = parseScore(user, year, term, type)
    except:
        data = []
    return render(request, 'grade/grade.html', {
        'grades': data,
        'current': current,
        })
