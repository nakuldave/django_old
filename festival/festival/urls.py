from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^Startseite/', include('home.urls')),
    url(r'^Veranstaltungen/', include('events.urls')),
    url(r'^News/', include('news.urls')),
    # url(r'^$', 'festival.views.home', name='home'),
    # url(r'^festival/', include('festival.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
