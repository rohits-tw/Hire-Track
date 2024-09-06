from rest_framework import serializers
from mom.models import Mom


class MomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mom
        fields = [
            "interview_id",
            "author_id",
            "notes",
            "action_items",
            "next_step",
            "created_at",
        ]


class UpdateMomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mom
        fields = ["notes", "action_items", "next_step", "updated_at"]


class GetAllMomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mom
        fields = [
            "id",
            "interview_id",
            "author_id",
            "notes",
            "action_items",
            "next_step",
            "created_at",
        ]
