# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView)

from crm_app.models import Account, Contact, Project, Meeting
from .serializers import (AddAccountSerializer, AddContactSerializer, AddProjectSerializer, AddMeetingSerializer,
                          ListAllMeetingsSerializer, DetailMeetingSerializer, ListAllAccountsSerializer,
                          DetailAccountSerializer, ListAllContactsSerializer, DetailContactSerializer,
                          ListAllProjectsSerializer, DetailProjectSerializer)


class AddAccountAPIView(CreateAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Account.objects.all()
    serializer_class = AddAccountSerializer


class AddContactAPIView(CreateAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Contact.objects.all()
    serializer_class = AddContactSerializer


class AddProjectAPIView(CreateAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Project.objects.all()
    serializer_class = AddProjectSerializer


class AddMeetingAPIView(CreateAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Meeting.objects.all()
    serializer_class = AddMeetingSerializer


class ViewAllMeetingsListAPIView(ListAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Meeting.objects.all().order_by('date')[::-1]
    serializer_class = ListAllMeetingsSerializer


# class ViewMeetingDetailAPIView(RetrieveAPIView):
#     # queryset = Meeting.objects.filter(account_company_name__company_name=company_name)
#     # TO DO: queryset to extract data and serialize it using company name.
#     queryset = Meeting.objects.all()
#     serializer_class = DetailMeetingSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'pk'


class ViewMeetingDetailAPIView(ListAPIView):
    # queryset = Meeting.objects.filter(account_company_name__company_name=company_name)
    # TO DO: queryset to extract data and serialize it using company name.
    # queryset = Meeting.objects.all()
    serializer_class = DetailMeetingSerializer

    # lookup_field = 'account_company_name'
    # lookup_url_kwarg = 'company_name'

    def get_queryset(self, **kwargs):
        # print(self.args)
        # print(self.kwargs['company_name'])
        if self.kwargs.get('meeting_id', None):
            queryset_list = Meeting.objects.filter(account_company_name__company_name=self.kwargs['company_name'],
                                                   id=self.kwargs['meeting_id'])
        else:
            queryset_list = Meeting.objects.filter(account_company_name__company_name=self.kwargs['company_name'])

        return queryset_list


class ViewAllAccountsListAPIView(ListAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Account.objects.all().order_by('status')
    serializer_class = ListAllAccountsSerializer


class ViewAccountDetailAPIView(RetrieveAPIView):
    # queryset = Meeting.objects.filter(account_company_name__company_name=company_name)
    # TO DO: queryset to extract data and serialize it using company name.
    queryset = Account.objects.all()
    serializer_class = DetailAccountSerializer
    lookup_field = 'company_name'
    lookup_url_kwarg = 'company_name'


class ViewAllContactsListAPIView(ListAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ListAllContactsSerializer


class ViewContactDetailAPIView(ListAPIView):
    serializer_class = DetailContactSerializer

    # lookup_field = 'id'
    # lookup_url_kwarg = 'contact_id'

    def get_queryset(self, **kwargs):
        # print(self.args)
        # print(self.kwargs['company_name'])
        if self.kwargs.get('contact_id', None):
            queryset_list = Contact.objects.filter(account_company_name__company_name=self.kwargs['company_name'],
                                                   id=self.kwargs['contact_id'])
        else:
            queryset_list = Contact.objects.filter(account_company_name__company_name=self.kwargs['company_name'])
        return queryset_list


class ViewAllProjectsListAPIView(ListAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Project.objects.all().order_by('notes')
    serializer_class = ListAllProjectsSerializer


class ViewProjectDetailAPIView(ListAPIView):
    serializer_class = DetailProjectSerializer

    def get_queryset(self, **kwargs):
        # print(self.args)
        # print(self.kwargs['company_name'])
        if self.kwargs.get('project_name', None):
            queryset_list = Project.objects.filter(account_company_name__company_name=self.kwargs['company_name'],
                                                   name=self.kwargs['project_name'])
        else:
            queryset_list = Project.objects.filter(account_company_name__company_name=self.kwargs['company_name'])
        return queryset_list
