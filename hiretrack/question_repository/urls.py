from django.urls import path
from question_repository.views import CreateQuestionView

urlpatterns = [
    path("create-question/", CreateQuestionView.as_view(), name="create-question"),
]