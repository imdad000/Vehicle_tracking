
from django.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	
    url(r'^admin/', admin.site.urls),
    url(r'^Dashboard/',include('Dashboard.urls')),
    url(r'^$', include('Dashboard.urls')),
]
