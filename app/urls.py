from django.conf.urls import patterns,url
#from django.conf.urls import url

from app.views import *

urlpatterns = patterns('',
    url(r'^login/',loginUsuario,name='loginUsuario',),
    url(r'^fetch_data/', fetch_data, name='get_data'),
    url(r'^home/(?P<anystring>.+)/', homeView,name='homeView',),
)
