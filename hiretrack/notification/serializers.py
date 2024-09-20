from rest_framework import serializers
from notification.models import Remainder, Notification


class RemainderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = "__all__"


class RemainderAsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = ["status"]


class NotificationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = "__all__"
