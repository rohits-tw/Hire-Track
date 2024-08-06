from rest_framework import generics, status, permissions
from .models import UserDetail, CustomUser
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    GetUserSerializers,
    UpdateUserSerializer,
    AddUserDetailSerializers,
    ChangePasswordSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
)
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from .query import get_all_user, get_user
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
import uuid


class RegisterUserAPIView(generics.CreateAPIView):
    """API view for registering a new user.

    This view handles user registration by accepting user data, validating it,
    and creating a new user. Upon successful registration, it returns a response
    containing the user's data along with JWT tokens (refresh and access).
    """

    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "status": True,
                "msg": "User created successfully.",
                "user": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )


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
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    

        
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
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetUser(APIView):
    """
    API view to retrieve user(s). If an ID is provided, retrieves a specific user.
    Otherwise, retrieves all users.
    """

    def get(self, request, id=None):
        if id:
            user = get_user(id)
            if not user:
                return Response({"status": False, "msg": "User does not exist"})
            serializer = GetUserSerializers(user, many=False)
            return Response(
                {"status": True, "msg": "User fetched.", "data": serializer.data}
            )

        all_users = get_all_user()
        serializer = GetUserSerializers(all_users, many=True)
        return Response(
            {"status": True, "msg": "Users fetched.", "data": serializer.data}
        )


class UpdateUserDetailView(generics.UpdateAPIView):
    """
    API view to update the details of the currently authenticated user's profile.

    This view allows an authenticated user to update their own profile details,
    including fields like `firstname`, `lastname`, `profile_picture`, `address`, etc.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateUserSerializer

    def get_object(self):
        """
        get_object():
        Retrieves the `UserDetail` instance related to the currently authenticated user.
        """
        return self.request.user.user_detail

    def put(self, request, *args, **kwargs):
        """
        put(request, *args, **kwargs):
        Handles PUT requests to update the `UserDetail` instance. Validates the
        provided data and saves the changes if the data is valid. If the data
        is not valid, it returns an error response.
        """
        try:
            user_detail = self.get_object()
            serializer = self.serializer_class(
                user_detail, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AddUserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    """
    View to handle adding user details for the currently authenticated user:
    This view handles POST requests to add user details for the logged-in user. 
    It checks if user details already exist and either saves the new details or returns an error.
    """

    def post(self, request):
        user = request.user
        data = request.data
        serializer = AddUserDetailSerializers(data=data)
        if UserDetail.objects.filter(user=user).exists():
            return Response(
                {"status": False, "msg": "Data Already Exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(
                {"status": True, "msg": "Data Saved"}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"status": False, "msg": "Data not saved", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    """
    Change the password for the authenticated user.

    **Process:**
    1. Validate the request data using the serializer.
    2. Verify the old password.
    3. Set the new password and save the user.
    """

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = request.user
                old_password = serializer.validated_data.get("old_password")
                new_password = serializer.validated_data.get("new_password")

                if user.check_password(old_password):
                    if old_password == new_password:
                        return Response(
                            {
                                "status": False,
                                "message": "New password should be different from the old password.",
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    user.set_password(new_password)
                    user.save()
                    return Response(
                        {"status": True, "message": "Password changed successfully."},
                        status=status.HTTP_200_OK,
                    )
                return Response(
                    {"status": False, "error": "Old password is incorrect."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ForgotPasswordView(APIView):
    """
    Validates the email, retrieves the user, generates a reset URL, and sends a reset email.

    **Responses:**
        - 200 OK: Password reset email sent successfully.
        - 400 Bad Request: Validation errors in the request data.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            user = get_object_or_404(CustomUser, email=email)
            key = uuid.uuid4().hex
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f"http://0.0.0.0:8000/api/user/reset-password/{uid}/{key}/"
            send_mail(
                "Reset Your Password",
                f"Click the link to reset your password: {reset_url}",
                "no-reply@yourdomain.com",
                [email],
                fail_silently=False,
            )
            return Response(
                {"message": "Password reset email sent."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    """
    Validates the reset link, updates the user's password if valid, and returns appropriate responses.

    **Responses:**
        - 200 OK: Password reset successfully.
    """

    permission_classes = [AllowAny]

    def post(self, request, uidb64, key):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(CustomUser, pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        if user is not None:
            serializer = ResetPasswordSerializer(data=request.data)
            if serializer.is_valid():
                user.set_password(serializer.validated_data["password"])
                user.save()
                return Response(
                    {"message": "Password reset successfully."},
                    status=status.HTTP_200_OK,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"error": "Invalid reset link."}, status=status.HTTP_400_BAD_REQUEST
        )
