from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from crm_app import views

urlpatterns = [
#    url(r'^$', views.home),
    url(r'ajaxcall/', views.dynamic_dropdown),
    url(r'addmeeting/', views.add_meeting, name='add_meeting'),
    url(r'addproject/', views.add_project),
    url(r'addcontact/', views.add_contact),
    url(r'addaccount/', views.add_account),
    url(r'viewaccount/(?P<company_name>[a-zA-Z]+)/$', views.view_account, name='view_account'),
    url(r'viewallaccounts/', views.view_all_accounts, name='view_all_accounts'),
    # url(r'viewmeeting/(?P<company_name>[a-zA-Z]+)/(?P<date>[a-zA-Z0-9][ A-Za-z0-9_-]*)/$', views.view_meeting, name='view_meeting'),
    url(r'viewmeeting/(?P<company_name>[a-zA-Z]+)/$', views.view_meeting, name='view_meeting'),
    url(r'viewallmeetings/', views.view_all_meetings, name='view_all_meetings'),
    url(r'viewcontact/(?P<company_name>[a-zA-Z]+)/(?P<contact_id>\d+)$', views.view_contact, name='view_contact'),
    url(r'viewallcontacts/', views.view_all_contacts, name='view_all_contacts'),
    url(r'viewproject/(?P<company_name>[a-zA-Z]+)/(?P<project_name>[(a-zA-Z) (a-zA-Z)]+)$', views.view_project, name='view_project'),
    url(r'viewallprojects/', views.view_all_projects, name='view_all_projects'),
    url(r'home/', views.home),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^changepasswordlogin/', views.change_password_login, name='change_password_login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
