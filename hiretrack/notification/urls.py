from django.urls import path
from notification.views import (
    CreateNotificationView,
    GetAllNotificationById,
    DeleteNotificationView,
    ImmediateRemainderView,
    DeleteRemainderView,
    NotificationAsReadView,
)

urlpatterns = [
    path(
        "create-notification/",
        CreateNotificationView.as_view(),
        name="create-notification",
    ),
    path(
        "List-notification-By-User-Id/<int:id>/",
        GetAllNotificationById.as_view(),
        name="get-all-notification",
    ),
    path(
        "delete-notification/<int:id>/",
        DeleteNotificationView.as_view(),
        name="delete-notification/",
    ),
    path(
        "immediate-remainder/",
        ImmediateRemainderView.as_view(),
        name="immediate-remainder/",
    ),
    path(
        "delete-remainder/<int:id>/",
        DeleteRemainderView.as_view(),
        name="delete-remainder/",
    ),
    path(
        "mark-as-read/<int:id>/",
        NotificationAsReadView.as_view(),
        name="mark-as-read/",
    ),
]
