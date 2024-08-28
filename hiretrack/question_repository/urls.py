from django.urls import path
from question_repository.views import CreateQuestionView, GetQuestionsByTeamId

urlpatterns = [
    path("create-question/", CreateQuestionView.as_view(), name="create-question"),
    path(
        "get-question-by-team-id/<int:id>/",
        GetQuestionsByTeamId.as_view(),
        name="get_Questions_by_team_id",
    ),
]
