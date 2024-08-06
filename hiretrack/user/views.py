from rest_framework import generics
from .models import  UserDetail
from .serializers import UserDetailSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class GetUser(APIView):


    def get(self, request, id = None):
        if id is not None:
            user_obj = self.fetch_user(id=id)

            if not user_obj:
                return Response({"status":False, "msg":"User does not exists"})
                        
            serializer = UserDetailSerializer(user_obj)
            return Response({"status":True, "msg":"Users fetched.", "data":serializer.data})
        
        user_objs = UserDetail.objects.all()
        serializer = UserDetailSerializer(user_objs, many = True)
        return Response({"status":True, "msg":"Users fetched.", "data":serializer.data})
    

    def fetch_user(self, id):
        try:
            user_obj = UserDetail.objects.get(id = id)
            return user_obj
        except UserDetail.DoesNotExist:
            return None

    
