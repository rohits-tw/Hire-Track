from rest_framework import serializers
from notification.models import Remainder


class RemainderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = "__all__"


class RemainderAsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = ["status"]
