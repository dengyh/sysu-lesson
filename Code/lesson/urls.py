from django.conf.urls import patterns, url


from lesson import views

urlpatterns = patterns('',
    url(r'^$', views.lessons_list, name='lessons_list'),
    url(r'^(?P<lesson_id>\d+)/$', views.lesson_detail, name='lesson_detail'),
    url(r'^home/$', views.select_result, name='select_result'),
)
