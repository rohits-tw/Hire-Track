from django.urls import path
from .backends import  TokenRefreshView
from .views import LoginAPIView, LogoutAPIView,RegisterUserAPIView, GetUser,UpdateUserDetailView , AddUserDetailView


   

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    # Above URL is used to run login and logout api 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # token/refresh is used to refresh tocken 
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    # Above URL is used to register new user
    path('get-user/<int:id>/', GetUser.as_view(), name='get-user'),
    path('get-all-user/', GetUser.as_view(), name='get-all-user'),
    # Above 2 URL is used to get the details of user 
    path('update-user/', UpdateUserDetailView.as_view(), name='update-user'),
    # Above URL is used to update user details 
    path('add-user-detail/', AddUserDetailView.as_view(), name='add-user-detail'),
]



