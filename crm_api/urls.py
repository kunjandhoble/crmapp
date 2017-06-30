from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from crm_api import views
urlpatterns = [
   url(r'^$', views.apihome),
]