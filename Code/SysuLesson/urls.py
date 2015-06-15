from django.conf.urls import include, url
from django.contrib import admin

import settings

urlpatterns = [
    url(r'', include('base.urls', namespace='base')),
    url(r'^comment/', include('comment.urls', namespace='comment')),
    url(r'^exchange/', include('exchange.urls', namespace='exchange')),
    url(r'^grade/', include('grade.urls', namespace='grade')),
    url(r'^lesson/', include('lesson.urls', namespace='lesson')),
    url(r'^meterial/', include('meterial.urls', namespace='meterial')),
    url(r'^school/', include('school.urls', namespace='school')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }, name='media'),
]
