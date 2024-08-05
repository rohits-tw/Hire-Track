from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# class MyModelListCreate(generics.ListCreateAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

# class MyModelDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer


class UserGetAPI(APIView):
    def get(self, request, id = None):
        if id is not None:
            try:
                object = MyModel.objects.get(id = id)
            except MyModel.DoesNotExist:
                return Response({"status":False, "msg":"User does not exists"})
            serializer = MyModelSerializer(object)
            return Response({"status":True, "msg":"Users fetched.", "data":serializer.data})
        objects = MyModel.objects.all()
        serializer = MyModelSerializer(objects, many = True)
        return Response({"status":True, "msg":"Users fetched.", "data":serializer.data})
    
