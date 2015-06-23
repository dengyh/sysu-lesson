from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_personal_grade, name='grade'),
]
