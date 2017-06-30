# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.

class user(models.Model):
    user_id = models.OneToOneField('User', on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = 'User'


class Account(models.Model):
    company_name = models.CharField(primary_key=True, max_length=200, db_column='Company name')
    status = models.TextField(db_column='Status', blank=False, null=False)
    category = models.TextField(db_column='Category', blank=False, null=False)

    class Meta:
        db_table = 'Account'

    def __str__(self):
        return '%s' % (self.company_name)


class Contact(models.Model):
    account_company_name = models.ForeignKey('Account', on_delete=models.CASCADE, db_column='account_companyname')
    name = models.CharField(db_column='Contact name', max_length=120, blank=False, null=False)
    email = models.EmailField(unique= True, db_column='Email', blank=False, null=False)
    phone = models.CharField(unique=True, max_length=10, validators=[RegexValidator(r'^\d{10}|(\d{5}[\-]\d{6})$')],
                             db_column='Phone', blank=False, null=False) #'\d{10}+|\d{5}([- ]*)\d{6}'  it worked - '\d{10}'
                            # complete regex : ((\+*)((0[ -]+)*|(91 )*)(\d{12}+|\d{10}+))|\d{5}([- ]*)\d{6}
    notes = models.TextField()

    class Meta:
        db_table = 'Contact'
        unique_together = ('email','phone')

    def __str__(self):
        return '%s' % (self.name)

class Project(models.Model):
    account_company_name = models.ForeignKey('Account', on_delete=models.CASCADE, db_column='account_companyname')
    name = models.CharField(db_column='Project name', max_length=120, blank=False, null=False)
    notes = models.TextField()
    status = models.TextField(db_column='Status', blank=False, null=False)

    class Meta:
        db_table = 'Project'
        unique_together = ('account_company_name','name')

    def __str__(self):
        return '%s' % (self.name)


class Meeting(models.Model):
    account_company_name = models.ForeignKey('Account', on_delete=models.CASCADE, db_column='account_companyname')
    contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE, db_column='contact_id')
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    date = models.DateTimeField(db_column='Date', null=False)
    notes = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'Meeting'
        unique_together=('date','account_company_name')
