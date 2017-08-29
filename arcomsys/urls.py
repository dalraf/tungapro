from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.listarclientes, name='listarclientes'),
    url(r'addclientes/', views.addclientes, name='addclientes'),
    url(r'deletarclientes/(?P<pk>[0-9]+)/$', views.deletarcliente, name='deletarcliente'),
]