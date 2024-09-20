from django.urls import path
from notification.views import (
    DeleteNotificationView,
    ImmediateRemainderView,
    DeleteRemainderView,
    NotificationAsReadView,
)

urlpatterns = [
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
