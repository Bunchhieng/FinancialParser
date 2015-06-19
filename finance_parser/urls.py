from django.conf import settings
from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<symbol>[\w]+)/$', views.data, name='data'),
    url(r'^api/get_ticker/$', views.get_ticker, name='get_ticker'),
    url(r'^clicked/$', views.button_clicked, name='clicked'),
]

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )
