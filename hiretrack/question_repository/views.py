from django.shortcuts import render
from question_repository.serializers import (
    CreateQuestionsSerializer,
    GetQuestionSerializer,
)
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, APIException, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from question_repository.models import QuestionRepository
from question_repository.query import (
    get_question_by_team_id,
)


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


class GetQuestionsByTeamId(APIView):
    """
    View to handle list all interview according to the interviewer id for the currently authenticated user:
    This view handles GET requests to get all interview according to the interviewer id for the logged-in user.
    It checks if interview details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        questions = get_question_by_team_id(id)
        if not questions.exists():
            return Response(
                {"status": False, "message": "No Question Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = GetQuestionSerializer(questions, many=True)
        return Response({"status": True, "Questions": serializer.data})
