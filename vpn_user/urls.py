from django.conf.urls import patterns
from django.conf.urls import url

from vpn_user import views

urlpatterns = patterns('',
    url(r'^$', views.index, name ='index')
)
