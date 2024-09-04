from django.urls import path
from interview.views import (
    CreateInterviewsView,
    ListInterviewsView,
    ListAllInterviewsView,
    ListInterviewHistoryByUserId,
    UpdateInterviewStatusView,
)


urlpatterns = [
    path("create-interview/", CreateInterviewsView.as_view(), name="create-interview"),
    # Above url is to create/schedule interview
    path(
        "list-interview/<int:id>/", ListInterviewsView.as_view(), name="list-interview"
    ),
    # Above url is to list interview by id
    path(
        "list-all-interview/",
        ListAllInterviewsView.as_view(),
        name="list-all-interview",
    ),
    # Above url is to list all interview
    path(
        "List-Interview-By-User-Id/<int:id>/",
        ListInterviewHistoryByUserId.as_view(),
        name="list-all-interview",
    ),
    # Above url is to list all interview
    path(
        "status-update/<int:id>/",
        UpdateInterviewStatusView.as_view(),
        name="update-interview-status",
    ),
    #Above url is to update the status of interview 
]
