from django.urls import path
from .views import GetUser

urlpatterns = [
    path('get-user/<int:id>/', GetUser.as_view(), name='get-user'),
    path('get-user/', GetUser.as_view(), name='get-user'),

]



