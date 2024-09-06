from django.urls import path, re_path
from mom.views import (
    CreateMomView,
    GetMomByInterviewIdView,
    UpdateMomByInterviewIdView,
    GetAllMomView,
    DeleteMomView,
    SearchMomAPIView,
)

urlpatterns = [
    path("create-mom/", CreateMomView.as_view(), name="create-mom"),
    path(
        "get-mom-by-interview-id/<int:id>/",
        GetMomByInterviewIdView.as_view(),
        name="get-mom-by-interview-id",
    ),
    path(
        "update-mom-by-interview-id/<int:id>/",
        UpdateMomByInterviewIdView.as_view(),
        name="update-mom-by-interview-id",
    ),
    path("get-all-mom/", GetAllMomView.as_view(), name="get-all-mom"),
    path("delete-mom-by-id/<int:id>/", DeleteMomView.as_view(), name="get-all-mom"),
    path("serach/", SearchMomAPIView.as_view(), name="mom-view"),
]
