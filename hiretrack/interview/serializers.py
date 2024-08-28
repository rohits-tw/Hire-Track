from rest_framework import serializers
from interview.models import InterviewForUser


class CreateInterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewForUser
        fields = "__all__"


class ListInterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewForUser
        fields = "__all__"
