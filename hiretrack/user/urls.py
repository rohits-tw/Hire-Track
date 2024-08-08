from django.urls import path
from .backends import  TokenRefreshView
from .views import LoginAPIView, LogoutAPIView,RegisterUserAPIView, GetUserView, AddUserDetailView


   

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('get-user/<int:id>/', GetUserView.as_view(), name='get-user'),
    path('get-all-user/', GetUserView.as_view(), name='get-all-user'),
    path('add-user-detail/', AddUserDetailView.as_view(), name='add-user-detail'),


]



