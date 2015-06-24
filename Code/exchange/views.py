from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.utils import timezone
import datetime

from .models import Exchange
from lesson.models import Lesson
from api.sysu import Sysuer
from api.parser import parseResultOfCourseSelection, parseScore

@login_required
@require_GET
def all_exchanges(request):
    """ interface URL: /exchange/ """
    exchanges = Exchange.objects.all()
    paginator = Paginator(exchanges, 5)
    page = request.GET.get('page')
    try:
        exchanges_per_page = paginator.page(page)
    except PageNotAnInteger:
        exchanges_per_page = paginator.page(1)
    except EmptyPage:
        exchanges_per_page = paginator.page(paginator.num_pages)
    current_page = exchanges_per_page.number
    pages_num = paginator.num_pages
    pages = [current_page + i for i in xrange(-6, 10) if current_page + i > 0 and current_page + i <= pages_num]
    return render(request, 'exchange/all_exchanges.html',{
        'exchanges':exchanges_per_page,
        'pages':pages[:10]})

@login_required
@require_GET
def my_exchanges(request):
    """ interface URL: /exchange/home/ """
    user = request.user
    exchanges = user.exchange_set.all()
    return render(request, 'exchange/my_exchanges.html',{
        'exchanges':exchanges})

@login_required
@require_GET
def new_exchange(request):
    """ interface URL: /exchange/form/ """
    user = Sysuer(username=request.user.username,
        cookie=request.session['cookie'])
    data = parseResultOfCourseSelection(user)
    lessons = [lesson for lesson in data if lesson['xnd'] == '2014-2015' and lesson['xq'] == '3' and int(lesson['kclbm'])>20]
    return render(request, 'exchange/new_exchange.html', {
        'lessons': lessons,
        })

@login_required
@require_POST
def create_exchange(request):
    """ interface URL: /exchange/create/ """
    lessonOut = request.POST['lessonOut']
    user = request.user
    lessonIn = request.POST['lessonIn']
    phone = request.POST['phone']
    email = request.POST['email']
    time = timezone.now()
    deadlineList = request.POST['deadline'].split('-')
    deadline = datetime.datetime(int(deadlineList[0]),
            int(deadlineList[1]), int(deadlineList[2]))
    exchange = Exchange(
            user = user,
            lessonOut = lessonOut,
            lessonIn = lessonIn,
            phone = phone,
            email = email,
            description = '',
            time = time,
            deadline = deadline,
    )
    exchange.save()
    return HttpResponseRedirect(reverse('exchange:all_exchanges'))

@login_required
@require_POST
def finish_exchange(request, exchange_id):
    """ interface URL: /exchange/id/finish"""
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    exchange.finish()
    exchange.save()
    return HttpResponseRedirect(reverse('exchange:exchange_detail', args=(exchange.id, )))

@login_required
@require_POST
def cancel_exchange(request, exchange_id):
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    exchange.delete()
    return HttpResponseRedirect(reverse('exchange:my_exchanges'))

@login_required
@require_GET
def exchange_detail(request, exchange_id):
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    not_finished = not exchange.finished
    current_user = request.user == exchange.user
    display = not_finished and current_user
    print not_finished, current_user
    return render(request, 'exchange/exchange_detail.html',{
        'exchange': exchange,
        'display': display})
# Create your views here.
