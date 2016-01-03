from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'spl.views.home', name='home'),
    url(r'^hello/', 'spl.views.hello', name='hello'),
    (r'^books/', include('spl.urls')),
	url(r'^accounts/login/$', 'spl.views.login', name='login'),
	url(r'^accounts/auth/$', 'spl.views.auth_view', name='auth_view'),
	url(r'^accounts/logout/$', 'spl.views.logout', name='logout'),
	url(r'^accounts/loggedin/$', 'spl.views.loggedin', name='loggedin'),
	url(r'^accounts/invalid/$', 'spl.views.invalid', name='invalid'),
)