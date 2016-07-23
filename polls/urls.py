from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^$', 'polls.views.index', name='index'),
	url(r'^(?P<poll_id>[\w-]+)/$', views.detail, name='detail'),
)
