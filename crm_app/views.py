# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from time import strftime, time

from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template import RequestContext
from django.template.context_processors import request, csrf
from django.contrib import messages
from crm_app.form import *
from .models import *


def home(request):
    return render(request, 'crm_app/login.html')


def add_account(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = AccountForm(request.POST)
        args['form'] = form
        if form.is_valid():
            print form
            args['msg'] = messages.success(request, 'ACCOUNT ADDED SUCCESSFULLY')
            form.save()  # save account to database if form is valid
            return HttpResponseRedirect('/crmbasic/home/')
        else:
            args['form'] = AccountForm()
            args['msg'] = messages.error(request, 'SOMETHING WENT WRONG !! TRY AGAIN.')
            return render_to_response('crm_app/add_account.html', args, RequestContext(request))
    args['form'] = AccountForm()
    return render_to_response('crm_app/add_account.html', args, RequestContext(request))


def add_contact(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = ContactForm(request.POST)
        args['form'] = form
        if form.is_valid():
            print form
            args['msg'] = messages.success(request, 'CONTACT ADDED SUCCESSFULLY')
            form.save()  # save contact to database if form is valid
            cont_obj = Contact.objects.all().values()
            print(cont_obj)
            return HttpResponseRedirect('/crmbasic/home/')
        else:
            args['form'] = ContactForm()
            args['msg'] = messages.error(request, 'SOMETHING WENT WRONG !! TRY AGAIN.')
            print("here it comes")
            return render_to_response('crm_app/add_contact.html', args, RequestContext(request))
    args['form'] = ContactForm()
    return render_to_response('crm_app/add_contact.html', args, RequestContext(request))


def add_project(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        args['form'] = form
        if form.is_valid():
            print form
            args['msg'] = messages.success(request, 'CONTACT ADDED SUCCESSFULLY')
            form.save()  # save contact to database if form is valid
            return HttpResponseRedirect('/crmbasic/home/')
        else:
            args['form'] = ProjectForm()
            args['msg'] = messages.error(request, 'SOMETHING WENT WRONG !! TRY AGAIN.')
            return render_to_response('crm_app/add_project.html', args, RequestContext(request))
    args['form'] = ProjectForm()
    return render_to_response('crm_app/add_project.html', args, RequestContext(request))


@login_required
def add_meeting(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        print(request.user)
        form = MeetingForm(request.POST)
        args['form'] = form

        # form.data['datetimevalue']
        if form.is_valid():
            obj = Meeting()
            print form, "make it work"

            print request.POST.get('datetimevalue')
            obj.date = request.POST.get('datetimevalue')
            obj.account_company_name = form.cleaned_data['account_company_name']
            obj.notes = form.cleaned_data['notes']
            obj.project_id = form.cleaned_data['project_id']
            obj.contact_id = form.cleaned_data['contact_id']
            args['msg'] = messages.success(request, 'CONTACT ADDED SUCCESSFULLY')
            obj.save()  # save contact to database if form is valid
            return HttpResponseRedirect('/crmbasic/home/')
        else:
            args['form'] = MeetingForm()
            args['msg'] = messages.error(request, 'SOMETHING WENT WRONG !! TRY AGAIN.')
            print("here it comes")
            return render_to_response('crm_app/add_meeting.html', args, RequestContext(request))
    args['form'] = MeetingForm()
    return render_to_response('crm_app/add_meeting.html', args, RequestContext(request))


def dynamic_dropdown(request):
    if request.is_ajax():
        todo_items = ['Mow Lawn', 'Buy Groceries', ]
        # print(todo_items)
        com_name = request.GET.get('Item')
        name_email_list = Contact.objects.filter(account_company_name__company_name__contains=com_name).values_list(
            'name', 'email')
        name_email_list = [i[0] + '(' + i[1] + ')' for i in name_email_list]
        project_list = Project.objects.filter(account_company_name__company_name__contains=com_name,
                                              status__exact='active').values_list('name')
        project_list = [i[0] for i in project_list]
        data = json.dumps({'contact_list': name_email_list, 'project_list': project_list})

        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404


def view_account(request, company_name):
    args = {}
    if request.method == 'GET':
        com_name = company_name
        print(com_name)
        obj = Account.objects.get(company_name=com_name)
        contact_list = Contact.objects.filter(account_company_name__company_name=com_name).values_list()
        contact_ids_list = [i[0] for i in contact_list]
        contact_names = [i[2] for i in contact_list]
        project_list = Project.objects.filter(account_company_name__company_name=com_name).values_list()
        project_ids_list = [i[0] for i in project_list]
        project_names = [i[2] for i in project_list]
        meeting_list = Meeting.objects.filter(account_company_name__company_name=com_name,
                                              contact_id_id__in=contact_ids_list,
                                              project_id_id__in=project_ids_list).values_list()
        meeting_notes = [i[1] for i in meeting_list]

        args['contact_list'] = contact_list
        args['contact_names'] = contact_names
        args['project_list'] = project_list
        args['project_names'] = project_names
        args['meeting_list'] = meeting_list
        args['meeting_notes'] = meeting_notes
        args['account_obj'] = obj
        return render_to_response('crm_app/view_account.html', args, RequestContext(request))
    raise Http404


def view_all_accounts(request):
    args = {}
    if request.method == 'GET':
        all_accounts = Account.objects.all().order_by('status')
        args['all_accounts'] = all_accounts
        return render_to_response('crm_app/view_all_accounts.html', args, RequestContext(request))
    raise Http404


def view_all_meetings(request):
    args = {}
    if request.method == 'GET':
        all_meetings = Meeting.objects.all().order_by('date')[::-1]
        args['all_meetings'] = all_meetings
        return render_to_response('crm_app/view_all_meetings.html', args, RequestContext(request))
    raise Http404


# def view_meeting(request, company_name, date):
def view_meeting(request, company_name):
    args = {}
    if request.method == 'GET':
        # print(date)
        meeting_info = Meeting.objects.filter(account_company_name__company_name=company_name)
        args['meeting_info'] = meeting_info
        return render_to_response('crm_app/view_meeting.html', args, RequestContext(request))
    raise Http404


def view_all_contacts(request):
    args = {}
    if request.method == 'GET':
        all_contacts = Contact.objects.all()
        args['all_contacts'] = all_contacts
        return render_to_response('crm_app/view_all_contacts.html', args, RequestContext(request))
    raise Http404


def view_contact(request, company_name, id):
    args = {}
    if request.method == 'GET':
        contact_info = Contact.objects.filter(account_company_name__company_name=company_name, id=id)
        meeting_info  = Meeting.objects.filter(account_company_name__company_name=company_name, contact_id=id)
        args['contact_info'] = contact_info
        args['meeting_info'] = meeting_info
        return render_to_response('crm_app/view_contact.html', args, RequestContext(request))
    raise Http404


def view_all_projects(request):
    args = {}
    if request.method == 'GET':
        all_projects = Project.objects.all().values_list('account_company_name', 'name').order_by('name')
        args['all_projects'] = all_projects
        for i in all_projects:
            print(i)
        return render_to_response('crm_app/view_all_projects.html', args, RequestContext(request))
    raise Http404


def view_project(request, company_name, project_name):
    args = {}
    if request.method == 'GET':
        project_info = Project.objects.filter(account_company_name__company_name=company_name, name=project_name)
        contact_info = Contact.objects.filter(account_company_name__company_name=company_name)
        proj_lst = [i.id for i in project_info]
        con_lst = [i.id for i in contact_info]

        meeting_info = Meeting.objects.filter(account_company_name__company_name=company_name,
                                              project_id__in=proj_lst, contact_id__in=con_lst)
        print("more info")
        args['company_name'] = company_name
        args['project_info'] = project_info
        args['contact_info'] = contact_info
        args['meeting_info'] = meeting_info
        for i in meeting_info:
            print(i)

        return render_to_response('crm_app/view_project.html', args, RequestContext(request))
    raise Http404


def change_password(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        args['form'] = form
        u_name = request.user
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password1')
            u = User.objects.get(username__exact=u_name)
            print(u.username)

            if u.check_password(old_password):
                print('inside check')
                u.set_password(new_password)
                u.save()
                update_session_auth_hash(request, user)
                u_auth = authenticate(username=u_name, password=new_password)
                login(request,u_auth)
                # user = form.save()
                messages.success(request, 'Your password was successfully updated yippppeee!')
                return redirect('add_meeting')
            else:
                print('UNAUTHORISED USER',u_name)
                u = User.objects.get(username__exact=u_name)
                print(u.check_password('rockstar@31'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        args['form'] = PasswordChangeForm(request.user)
    return render(request, 'crm_app/change_password.html', args)

def change_password_login(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        args['form'] = form
        if form.is_valid():
            u_name = form.cleaned_data.get('username')
            print(u_name)
            password = form.cleaned_data.get('password')
            u_auth = authenticate(username=u_name, password = password)
            login(request,u_auth)
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = LoginForm()
        args['form'] = form
    return render(request, 'crm_app/change_password_login.html', args)