from django import forms

from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['company_name', 'status', 'category']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['account_company_name', 'name', 'email', 'phone', 'notes']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['account_company_name', 'name', 'notes', 'status']


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        exclude = ['date']


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password')
    class Meta:
        exclude=[]
        widgets = {
            'password': forms.PasswordInput(),
        }