from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'olymega'
urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^news/', views.news, name='news'),
    url(r'^events/', views.events, name='events'),
    url(r'^join/', views.join, name='join'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^bylaws/', views.bylaws, name='bylaws'),
    url(r'^donate/', views.donate, name='donate'),
    url(r'^forum/', views.forum, name='forum'),
    url(r'^projects/', views.projects, name='projects'),
]
