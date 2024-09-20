from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from notification.serializers import (
    RemainderSerializer,
    RemainderAsReadSerializer,
    NotificationSerializers,
)
from rest_framework.permissions import IsAuthenticated
from notification.models import Notification, Remainder
from notification.query import get_notification_details_by_id, get_by_remainder_id
from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException


# Create your views here.


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


class DeleteNotificationView(APIView):
    """
    View to handle delete notification for the currently authenticated user:
    This view handles DELETE requests to delete notification for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            notification = get_notification_details_by_id(id)
            notification.delete()
            return Response(
                {"status": True, "message": "Notification deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except Notification.DoesNotExist:
            return Response(
                {"status": False, "message": "Notification not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class DeleteRemainderView(APIView):
    """
    View to handle DELETE remainder for the currently authenticated user:
    This view handles DELETE request to delete remainder for the logged-in user.
    """

    def delete(self, request, id):
        try:
            remainder = get_by_remainder_id(id)
            remainder.delete()
            return Response(
                {"status": True, "message": "Remainder deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except Remainder.DoesNotExist:
            return Response(
                {"status": False, "message": "Remainder not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class NotificationAsReadView(APIView):
    """
    View to handle Mark Notification as Read for the currently authenticated user:
    This view handles POST request to Mark Notification as Read for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        try:
            remainder = get_by_remainder_id(id)
            serializer = RemainderAsReadSerializer(
                remainder, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": True,
                        "message": "Notification marked as read.",
                    }
                )
        except Remainder.DoesNotExist:
            return Response(
                {"status": False, "message": "Remainder id not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                {
                    "status": True,
                    "message": "notification",
                    "notification": serializer.data,
                }
            )
        except Notification.DoesNotExist:
            return Response(
                {"status": False, "message": "Notification ID not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class ImmediateRemainderView(APIView):
    """
    View to handle immediate remainder for the currently authenticated user:
    This view handles immediate remainder for the logged-in user.
    """

    def post(self, request):
        try:
            serializer = RemainderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Notification sent successfully.",
                    },
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))
