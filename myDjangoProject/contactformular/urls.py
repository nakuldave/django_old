from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contactformular.views.home'),
    url(r'^meldungen/$', 'contactformular.views.meldungen'),
    url(r'^get_meldung/(?P<person_id>\d+)/$', 'contactformular.views.meldung'),
    # url(r'^$', 'myDjangoProject.views.home', name='home'),
    # url(r'^myDjangoProject/', include('myDjangoProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
