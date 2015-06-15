from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Exchange

def all_exchanges(request):
    """ interface URL: /exchange/ """
    exchanges = Exchange.objects.all()
    paginator = Paginator(exchanges, 1)
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

def my_exchanges(request):
    """ interface URL: /exchange/home/ """
    exchanges = Exchange.objects.all()
    return render(request, 'exchange/my_exchanges.html',{
        'exchanges':exchanges})

def new_exchange(request):
    """ interface URL: /exchange/form/ """
    return render(request, 'exchange/new_exchange.html')

def create_exchange(request):
    """ interface URL: /exchange/create/ """
    return HttpResponseRedirect(reverse('exchange:all_exchanges'))

def finish_exchange(request, exchange_id):
    """ interface URL: /exchange/id/finish"""
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    exchange.finish()
    exchange.save()
    return HttpResponseRedirect(reverse('exchange:exchange_detail', args=(exchange.id, )))

def cancel_exchange(request, exchange_id):
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    exchange.cancel()
    exchange.save()
    return HttpResponseRedirect(reverse('exchange:exchange_detail', args=(exchange_id, )))

def exchange_detail(request, exchange_id):
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    if exchange.get_state() == 'i':
        not_finished = True
    else:
        not_finished = False
    return render(request, 'exchange/exchange_detail.html',{
        'exchange': exchange,
        'not_finished': not_finished})
# Create your views here.
