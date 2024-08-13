from django.urls import path
from Teams.views import CreateTeamView, GetTeamView, DeleteTeamView, UpdateTeamView, GetAllTeamView


urlpatterns = [
    path("create-team/", CreateTeamView.as_view(), name="create-team"),
    # Above URL is used to create team
    path("get-team/<int:id>/", GetTeamView.as_view(), name="get-team"),
    # Above URL is used to get team
    path("get-all-team/", GetAllTeamView.as_view(), name="get-all-team"),
    # Above URL is used to get all teams
    path("update-team/<int:id>/", UpdateTeamView.as_view(), name="update-team"),
    # Above URL is used to update team
    path("delete-team/<int:id>/", DeleteTeamView.as_view(), name="del-team"),
    # Above URL is used to delete team
]
