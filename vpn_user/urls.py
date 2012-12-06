from django.conf.urls import patterns
from django.conf.urls import url

from vpn_user import views

urlpatterns = patterns('',
    url(r'^register$', views.register, name='register'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^user_info$', views.user_info, name='user_info'),
    url(r'^user_log$', views.user_log, name='user_log'),
    url(r'^base$', views.base, name='base'),
    url(r'^enable_disable$', views.enable_disable, name='enable_disable'),
    url(r'^$', views.index, name='index'),
)
