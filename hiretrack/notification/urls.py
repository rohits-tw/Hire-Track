from django.urls import path
from notification.views import (
    CreateNotificationView,
    GetAllNotificationById,
)

urlpatterns = [
    path("create-notification/", CreateNotificationView.as_view(), name="create-notification"),
    path("List-notification-By-User-Id/<int:id>/", GetAllNotificationById.as_view(), name="get-all-notification"),
]
