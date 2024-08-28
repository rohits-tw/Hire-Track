from django.shortcuts import render
from question_repository.serializers import (
    CreateQuestionsSerializer,
)
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, APIException, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from question_repository.models import QuestionRepository


class CreateQuestionView(APIView):
    """
    View to handle create Question:
    This view handles POST requests to create Questions repository.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = CreateQuestionsSerializer(data=request.data)
            if serializer.is_valid():
                Question = serializer.save()
                return Response(
                    {
                        "question_id": str(Question.id),
                        "message": "Question added successfully",
                    },
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))