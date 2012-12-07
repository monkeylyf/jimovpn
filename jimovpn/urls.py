from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jimovpn.views.home', name='home'),
    # url(r'^jimovpn/', include('jimovpn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('vpn_user.urls')),
    url(r'^$', 'vpn_user.views.index')
)
