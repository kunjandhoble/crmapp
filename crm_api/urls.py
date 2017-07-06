from django.conf.urls import url

from crm_api.views import (
    AddMeetingAPIView, AddProjectAPIView, AddContactAPIView, AddAccountAPIView,
    ViewAllMeetingsListAPIView, ViewMeetingDetailAPIView, ViewAllAccountsListAPIView,
    ViewAccountDetailAPIView, ViewAllContactsListAPIView, ViewContactDetailAPIView, ViewAllProjectsListAPIView,
    ViewProjectDetailAPIView)

urlpatterns = [
    url(r'addmeetingapi/', AddMeetingAPIView.as_view(), name='add_meeting_api'),
    url(r'addprojectapi/', AddProjectAPIView.as_view(), name='add_project_api'),
    url(r'addcontactapi/', AddContactAPIView.as_view(), name='add_contact_api'),
    url(r'addaccountapi/', AddAccountAPIView.as_view(), name='add_account_api'),
    url(r'^viewallmeetingsapi/', ViewAllMeetingsListAPIView.as_view(), name='view_allmeetings_api'),
    # url(r'viewmeetingapi/(?P<pk>\d+)/$', ViewMeetingDetailAPIView.as_view(), name='view_meeting_api'),
    url(r'viewmeetingapi/(?P<company_name>[a-zA-Z]+)/(?P<meeting_id>\d+)$', ViewMeetingDetailAPIView.as_view(),
        name='view_meeting_api'),
    url(r'viewmeetingapi/(?P<company_name>[a-zA-Z]+)/$', ViewMeetingDetailAPIView.as_view(),
        name='view_companymeeting_api'),
    url(r'^viewallaccountsapi/', ViewAllAccountsListAPIView.as_view(), name='view_allaccounts_api'),
    url(r'viewaccountapi/(?P<company_name>[a-zA-Z]+)/$', ViewAccountDetailAPIView.as_view(),
        name='view_account_api'),
    url(r'^viewallcontactsapi/', ViewAllContactsListAPIView.as_view(), name='view_allcontacts_api'),
    url(r'viewcontactapi/(?P<company_name>[a-zA-Z]+)/(?P<contact_id>\d+)$', ViewContactDetailAPIView.as_view(),
        name='view_contact_api'),
    url(r'viewcontactapi/(?P<company_name>[a-zA-Z]+)', ViewContactDetailAPIView.as_view(),
        name='view_companycontact_api'),
    url(r'^viewallprojectsapi/', ViewAllProjectsListAPIView.as_view(), name='view_allprojects_api'),
    url(r'viewprojectapi/(?P<company_name>[a-zA-Z]+)/(?P<project_name>[(a-zA-Z) (a-zA-Z)]+)/$',
        ViewProjectDetailAPIView.as_view(), name='view_project_api'),
    url(r'viewprojectapi/(?P<company_name>[a-zA-Z]+)',
        ViewProjectDetailAPIView.as_view(), name='view_companyproject_api'),
]
