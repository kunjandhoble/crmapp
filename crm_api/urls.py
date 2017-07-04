from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from views import *

urlpatterns = [
    url(r'^viewallmeetingsapi/', ViewAllMeetingsListAPIView.as_view(), name='view_allmeetings_api'),
    url(r'viewmeetingapi/(?P<pk>\d+)/$', ViewMeetingDetailAPIView.as_view(), name='view_meeting_api'),
]
