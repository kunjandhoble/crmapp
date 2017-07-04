# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
    )

from crm_app.models import Meeting
from .serializers import (
    ListAllMeetingsSerializer,
    DetailMeetingSerializer
    )


class ViewAllMeetingsListAPIView(ListAPIView):
    # account_company_name = serializers.SerializerMethodField()
    queryset = Meeting.objects.all().order_by('date')[::-1]
    serializer_class = ListAllMeetingsSerializer


class ViewMeetingDetailAPIView(RetrieveAPIView):
    # queryset = Meeting.objects.filter(account_company_name__company_name=company_name)
    queryset = Meeting.objects.all()
    serializer_class = DetailMeetingSerializer
