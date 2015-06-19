from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_exchanges, name='all_exchanges'),
    url(r'^home/$', views.my_exchanges, name='my_exchanges'),
    url(r'^form/$', views.new_exchange, name='new_exchange'),
    url(r'^create/$', views.create_exchange, name='create_exchange'),
    url(r'^(?P<exchange_id>[0-9]+)/finish/$', views.finish_exchange, name='finish_exchange'),
    url(r'^(?P<exchange_id>[0-9]+)/cancel/$', views.cancel_exchange, name='cancel_exchange'),
    url(r'^(?P<exchange_id>[0-9]+)/$', views.exchange_detail, name='exchange_detail'),
]
