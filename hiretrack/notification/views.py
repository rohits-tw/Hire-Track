from django.shortcuts import render
from notification.serializers import (
    NotificationSerializers,
)
from rest_framework.response import Response
from rest_framework import status
from notification.models import Notification
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.permissions import IsAuthenticated
from notification.query import (
    get_notification_details_by_id
)

class CreateNotificationView(APIView):
    """
    View to handle create notification for the currently authenticated user:
    This view handles POST requests to create notification to send to the candidate.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = NotificationSerializers(data=request.data)
            if serializer.is_valid():
                notification = serializer.save()
                return Response(
                    {
                        "message": "Notification created successfully.",
                        "notification_id": str(notification.id),
                    },
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))


class GetAllNotificationById(APIView):
    """
    View to handle get notification by id for the currently authenticated user:
    This view handles GET requests to get all notificaton for the logged-in user.
    It checks if notification details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            notification_by_id = get_notification_details_by_id(id)
            serializer = NotificationSerializers(notification_by_id)
            return Response(
                {"status": True, "message": "notification", "notification": serializer.data}
            )
        except Notification.DoesNotExist:
            return Response(
                {"status": False, "message": "Notification ID not found"},
                status=status.HTTP_404_NOT_FOUND,
            )