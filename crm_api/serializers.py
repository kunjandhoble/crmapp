from rest_framework.serializers import ModelSerializer

from crm_app.models import Meeting


class ListAllMeetingsSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        exclude = ['project_id']

class DetailMeetingSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        exclude = ['project_id']

