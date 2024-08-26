from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    CreateInterviewSerializer)
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError,APIException
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateInterviewsView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = CreateInterviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Interview scheduled successfully",},
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))
