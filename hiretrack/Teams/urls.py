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
    # Above URL is used to create team
    path("get-team/<int:id>/", GetTeamView.as_view(), name="get-team"),
    # Above URL is used to get team by id
    path(
        "team-members/",
        TeamMembersListCreateView.as_view(),
        name="team-members-create",
    ),
    # Above URL is used to create team member
    path(
        "get-team-members/<int:team_id>/",
        TeamMembersListCreateView.as_view(),
        name="team-members-list",
    ),
    # Above URL is used to get members alloted team wise
    path(
        "delete-team-member/<int:id>/",
        TeamMembersDeleteView.as_view(),
        name="team-members--delete",
    ),
    # Above URL is used to delete team members
    path("get-all-team/", GetAllTeamView.as_view(), name="get-all-team"),
    # Above URL is used to get all teams
    path("update-team/<int:id>/", UpdateTeamView.as_view(), name="update-team"),
    # Above URL is used to update team
    path("delete-team/<int:id>/", DeleteTeamView.as_view(), name="del-team"),
    # Above URL is used to delete team
]
