from django.urls import path
from Teams.views import (
    CreateTeamView,
    GetTeamView,
    DeleteTeamView,
    TeamMembersListCreateView,
    TeamMembersDeleteView,
    UpdateTeamView,
    GetAllTeamView,
)


urlpatterns = [
    path("create-team/", CreateTeamView.as_view(), name="create-team"),
    path("get-team/<int:id>/", GetTeamView.as_view(), name="get-team"),
    path(
        "team-members/",
        TeamMembersListCreateView.as_view(),
        name="team-members-list-create",
    ),
    path(
        "delete-team-member/<int:id>/",
        TeamMembersDeleteView.as_view(),
        name="team-members--delete",
    ),
    # Above URL is used to get team
    path("get-all-team/", GetAllTeamView.as_view(), name="get-all-team"),
    # Above URL is used to get all teams
    path("update-team/<int:id>/", UpdateTeamView.as_view(), name="update-team"),
    # Above URL is used to update team
    path("delete-team/<int:id>/", DeleteTeamView.as_view(), name="del-team"),
    # Above URL is used to delete team
]
