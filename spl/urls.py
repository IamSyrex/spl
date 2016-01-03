from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'spl.views.home', name='home'),
    url(r'^all/$', 'spl.views.books'),
    url(r'^get/(?P<book_id>\d+)/$', 'spl.views.book'),
)