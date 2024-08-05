from django.urls import path
from .views import LoginAPIView, LogoutAPIView, TokenRefreshView, DummyView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
