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
    year = request.GET.get('year', None)
    term = request.GET.get('term', None)
    user = Sysuer(username=request.user.username,
        cookie=request.session['cookie'])
    data = parseScore(user, year, term)
    return render(request, 'grade/grade.html', {
        'grades': data,
        })