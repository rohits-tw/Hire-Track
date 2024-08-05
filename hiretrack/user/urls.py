from django.urls import path
from .views import UserGetAPI

urlpatterns = [
    path('GetUser/<int:id>/', UserGetAPI.as_view(), name='GetWithID'),
    path('GetUser/', UserGetAPI.as_view(), name='GetWithoutID'),

]



