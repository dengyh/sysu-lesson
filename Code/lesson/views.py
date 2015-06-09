from django.shortcuts import render
from django.http import Http404

from .models import Lesson

# Create your views here.
def lessons_list(request):
    lessons = Lesson.objects.all()[:100]
    return render(request, 'lesson/lessons_list.html', {'lessons': lessons})

def lesson_detail(request, lesson_id):
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
    except Lesson.DoesNotExist:
        raise Http404('Lesson does not exist...')
    return render(request, 'lesson/lesson_detail.html', {'lesson': lesson})
