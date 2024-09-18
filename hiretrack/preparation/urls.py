from django.urls import path
from preparation.views import (
    AddPreparationView,
    GetAllMaterialView,
    GetMaterialByIdView,
    UpdateMaterialView,
    DeleteMaterialView,
    SearchMaterialView,
    AddBookMarkView,
    DeleteBookMarkView,
    GetBookMarkByUserIdView,
)


urlpatterns = [
    path("add-preparation/", AddPreparationView.as_view(), name="add-preparation"),
    # Above URL is used to add preperation
    path(
        "get-all-preparation/",
        GetAllMaterialView.as_view(),
        name="get-all-preparation/",
    ),
    # Above URL is used to get all preperation
    path(
        "get-preparation/<int:id>/",
        GetMaterialByIdView.as_view(),
        name="get-preparation/",
    ),
    # Above URL is used to get preperation by id
    path(
        "update-preparation/<int:id>/",
        UpdateMaterialView.as_view(),
        name="update-preparation/",
    ),
    # Above URL is used to update preperation
    path(
        "delete-preparation/<int:id>/",
        DeleteMaterialView.as_view(),
        name="delete-preparation/",
    ),
    # Above URL is used to delete preperation by id
    path(
        "search-preparation/",
        SearchMaterialView.as_view(),
        name="search-preparation/",
    ),
    # Above URL is used to search preperation by type and tag and keyword
    path(
        "add-bookmark/",
        AddBookMarkView.as_view(),
        name="add-bookmark/",
    ),
    # Above URL is used to add bookmark to preperation
    path(
        "delete-bookmark/<int:id>/",
        DeleteBookMarkView.as_view(),
        name="delete-bookmark/",
    ),
    # Above URL is used to delete bookmark to preperation
    path(
        "get-bookmark-by-userid/<int:id>/",
        GetBookMarkByUserIdView.as_view(),
        name="get-bookmark-by-userid/",
    ),
    # Above URL is used to get bookmark by user-id
]
