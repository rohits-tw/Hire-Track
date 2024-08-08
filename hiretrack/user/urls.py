from django.urls import path
from .backends import  TokenRefreshView
from .views import LoginAPIView, LogoutAPIView,RegisterUserAPIView, GetUser,UpdateUserDetailView


   

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('get-user/<int:id>/', GetUser.as_view(), name='get-user'),
    path('get-all-user/', GetUser.as_view(), name='get-all-user'),
    path('update-user/', UpdateUserDetailView.as_view(), name='update-user'),
]



