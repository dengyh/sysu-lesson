from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Lesson

# Create your views here.
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

def lesson_detail(request, lesson_id):
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
    except Lesson.DoesNotExist:
        raise Http404('Lesson does not exist...')
    return render(request, 'lesson/lesson_detail.html', {'lesson': lesson})
