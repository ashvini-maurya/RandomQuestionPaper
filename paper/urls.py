__author__ = 'ashvini'

from django.conf.urls import patterns, url
from paper import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^question/$', views.question, name='question'),
)
