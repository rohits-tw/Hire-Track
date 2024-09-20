from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("user.urls")),
    path("api/Teams/", include("Teams.urls")),
    path("api/interview/", include("interview.urls")),
    path("api/Question/", include("question_repository.urls")),
    path('api/mom/', include('mom.urls')),
    path("api/preparation/", include("preparation.urls")),
    path("api/notification/", include("notification.urls"))
]