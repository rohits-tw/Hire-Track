from rest_framework import generics,status,permissions
from .models import  UserDetail, CustomUser
from .serializers import UserDetailSerializer,LoginSerializer, RegisterSerializer, GetUserSerializers,AddUserDetailSerializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .query import get_all_user,get_user


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
                "status": True,
                "msg": "User created successfully.",
                "user": serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
      

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


class GetUserView(APIView):
    def get(self, request, id = None):
        if id:
            user = get_user(id)
            serializer = GetUserSerializers(user,many =True)

            if not user:
                return Response({"status":False, "msg":"User does not exists"})  
            return Response({"status":True, "msg":"Users fetched.", "data":serializer.data})     
        all_user=get_all_user()
        serializer = GetUserSerializers(all_user,many =True)

        return Response({"status":True, "msg":"Users fetched.", "data":serializer.data})


class AddUserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    """
    View to handle adding user details for the currently authenticated user:
    This view handles POST requests to add user details for the logged-in user. 
    It checks if user details already exist and either saves the new details or returns an error.
    """
    def post(self, request):
        user = request.user
        data = request.data.copy()  
        serializer = AddUserDetailSerializers(data=data)
        if UserDetail.objects.filter(user=user).exists():
            return Response({"status": False, "msg": "Data Already Exists"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({"status": True, "msg": "Data Saved"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": False, "msg": "Data not saved", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)