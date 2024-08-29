from django.urls import path
from question_repository.views import (
    CreateQuestionView,
    GetQuestionsByTeamIdView,
    UpdateQuestionByIdView,
)

urlpatterns = [
    path("create-question/", CreateQuestionView.as_view(), name="create-question"),
    path(
        "get-question-by-team-id/<int:id>/",
        GetQuestionsByTeamIdView.as_view(),
        name="get_Questions_by_team_id",
    ),
    path(
        "update-question-by-id/<int:id>/",
        UpdateQuestionByIdView.as_view(),
        name="update-quesion-by-id",
    ),
]
