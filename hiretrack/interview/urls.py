from django.urls import path
from interview.views import (
    CreateInterviewsView
)


urlpatterns = [
    path("create-interview/", CreateInterviewsView.as_view(), name="create-interview")
]
