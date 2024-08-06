# myapp/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, phone_number=None, password=None, **kwargs):
        if email:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return None
        elif username:
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                return None
        elif phone_number:
            try:
                user = CustomUser.objects.get(phone_number=phone_number)
            except CustomUser.DoesNotExist:
                return None
        else:
            return None

        if user.check_password(password):
            return user
        return None



class TokenRefreshView(generics.GenericAPIView):
    """
    Handles token refresh requests and returns a new access token.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Processes the token refresh request and returns a new access token if valid.
        
        :param request: The request object containing the refresh token.
        :return: A response containing the new access token if the refresh token is valid.
        """
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            access_token = token.access_token
            return Response({
                'access': str(access_token),
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)