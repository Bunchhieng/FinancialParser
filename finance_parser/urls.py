from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<symbol>[\w]+)/$', views.data, name='data'),
    url(r'^api/get_ticker/$', views.get_ticker, name='get_ticker'),
    url(r'^clicked/$', views.button_clicked, name='clicked'),
]
