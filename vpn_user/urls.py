from django.conf.urls import patterns
from django.conf.urls import url

from vpn_user import views

urlpatterns = patterns('',
    url(r'^register$', views.register, name='register'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^user_info$', views.user_info, name='user_info'),
    url(r'^enable_user$', views.enable_user, name='enable_user'),
    url(r'^disable_user$', views.disable_user, name='disable_user'),
    url(r'^$', views.index, name='index'),
)
