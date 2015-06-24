from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from .models import Lesson
from comment.models import Comment
from meterial.models import Meterial
from api.myLesson import MyLesson
from api.sysu import Sysuer
from api.parser import parseResultOfCourseSelection, parseScore

# Create your views here.
@require_GET
@login_required
def lessons_list(request):
    search = request.GET.get('p', None)
    if search is not None:
        all_lessons = Lesson.objects.filter(Q(title__contains=search) | Q(teacher__contains=search))
    else:
        all_lessons = Lesson.objects.all()
    paginator = Paginator(all_lessons, 25)

    page = request.GET.get('page')
    try:
        lessons = paginator.page(page)
    except PageNotAnInteger:
        lessons = paginator.page(1)
    except EmptyPage:
        lessons = paginator.page(paginator.num_pages)

    return render(request, 'lesson/lessons_list.html', {
        'lessons': lessons,
        'search': search,
        })


@login_required
@require_GET
def lesson_detail(request, lesson_id):
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
    except Lesson.DoesNotExist:
        raise Http404('Lesson does not exist...')
    user = request.user
    comments = Comment.objects.filter(user=user).filter(lesson=lesson)
    meterials = Meterial.objects.filter(lesson=lesson)
    return render(request, 'lesson/lesson_detail.html', {
        'lesson': lesson,
        'comments': comments,
        'meterials': meterials,
    })

@login_required
@require_GET
def select_result(request):
    user = Sysuer(username=request.user.username,
        cookie=request.session['cookie'])
    lessons = parseResultOfCourseSelection(user)
    for x in lessons:
        try:
            lesson = Lesson.objects.get(lessonId=x['kch'], teacher=x['xm'])
            x.set('id', lesson.id)
        except:
            pass
    return render(request, 'lesson/select_result.html', {
        'lessons': lessons,
    })
