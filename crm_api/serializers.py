from rest_framework.serializers import ModelSerializer

from crm_app.models import Meeting, Account, Contact, Project


class AddAccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        exclude = []


class AddContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        exclude = []


class AddProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        exclude = []


class AddMeetingSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        exclude = []


class ListAllMeetingsSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        exclude = ['project_id']


class DetailMeetingSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        exclude = ['project_id']


#
class ListAllAccountsSerializer(ModelSerializer):
    class Meta:
        model = Account
        exclude = []


class DetailAccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        exclude = []


#
class ListAllContactsSerializer(ModelSerializer):
    class Meta:
        model = Contact
        exclude = []


class DetailContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        exclude = []


#
class ListAllProjectsSerializer(ModelSerializer):
    class Meta:
        model = Project
        exclude = []


class DetailProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        exclude = []
