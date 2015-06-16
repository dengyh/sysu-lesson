from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Lesson
from comment.models import Comment
from meterial.models import Meterial

# Create your views here.
@require_GET
@login_required
def lessons_list(request):
    all_lessons = Lesson.objects.all()
    paginator = Paginator(all_lessons, 25)

    page = request.GET.get('page')
    try:
        lessons = paginator.page(page)
    except PageNotAnInteger:
        lessons = paginator.page(1)
    except EmptyPage:
        lessons = paginator.page(paginator.num_pages)

    return render(request, 'lesson/lessons_list.html', {'lessons': lessons})


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
