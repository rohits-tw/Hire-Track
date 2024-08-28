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


class ListAllInterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewForUser
        fields = [
            "id",
            "user_id",
            "interviewer_id",
            "interview_date",
            "interview_type",
            "status",
        ]


class ListInterviewHistoryByUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewForUser
        fields = ["id", "interview_date", "interview_type", "status", "notes"]
