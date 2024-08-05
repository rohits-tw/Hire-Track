# myapp/views.py
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import LoginSerializer

class LoginAPIView(generics.GenericAPIView):
    """
    Handles user login and returns a refresh and access token.
    """
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Processes the login request and returns tokens if valid.
        
        :param request: The request object containing the user credentials.
        :return: A response containing the refresh and access tokens if the credentials are valid.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    

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
        
class LogoutAPIView(generics.GenericAPIView):
    """
    Handles user logout by blacklisting the refresh token.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Processes the logout request by blacklisting the refresh token.
        
        :param request: The request object containing the refresh token.
        :return: A response indicating the logout status.
        """
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

