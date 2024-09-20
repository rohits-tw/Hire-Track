from rest_framework import serializers
from notification.models import Notification, Remainder


class NotificationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = "__all__"


class RemainderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = "__all__"


class RemainderAsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = ["status"]
