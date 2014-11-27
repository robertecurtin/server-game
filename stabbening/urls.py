from django.conf.urls import patterns, url
from stabbening import views

urlpatterns = patterns('',
#        url(r'$', views.index, name='index'),
        url(r'^unit/(?P<unit_name_slug>[\w\-]+)/$', views.unit, name='unit'),   
        url(r'^city/(?P<city_name_slug>[\w\-]+)/$', views.city, name='city'),   
        url(r'^player/(?P<player_name_slug>[\w\-]+)/$', views.player, name='player'),   
        )
