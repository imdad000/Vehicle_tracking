
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [ 
    url(r'^$',views.detail,name='detail'),
    url(r'', views.detail, name='detail'),
	    
]