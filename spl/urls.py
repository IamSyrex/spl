from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'spl.views.books'),
	# url(r'^$', 'spl.views.home', name='home'),
    # url(r'^all/$', 'spl.views.books'),
    url(r'^details/(?P<book_slug>[\w-]+)/$', 'spl.views.book'),
)