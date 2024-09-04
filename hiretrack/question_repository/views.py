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
from question_repository.query import get_question_by_team_id, get_by_id


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


class GetQuestionsByTeamIdView(APIView):
    """
    API view to list all questions for a specific team ID for the authenticated user.

    Handles GET requests to retrieve all questions associated with a given team ID.
    Returns an error message if no questions are found.
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


class UpdateQuestionByIdView(APIView):
    """
    API view to update a question by its ID.

    This view allows authenticated users to partially update
    the details of a question identified by its ID.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = GetQuestionSerializer

    def post(self, request, id):
        try:
            question = get_by_id(id)
        except QuestionRepository.DoesNotExist:
            return Response(
                {"status": False, "message": "Question id not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(question, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "question_id": str(question.id),
                    "message": "Question updated successfully",
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetQuestionByIdView(APIView):
    """
    API view to get a question by its ID.

    This view allows authenticated users to get question by id
    the details of a question identified by its ID.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            question = get_by_id(id)
        except QuestionRepository.DoesNotExist:
            return Response(
                {"status": "False", "message": "Id Doesn't exists!!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = GetQuestionSerializer(question)
        return Response({"status": "True", "question": serializer.data})


class DeleteQuestionView(APIView):
    """
    API view to delete a question by its ID.

    This view allows authenticated users to delete question by id
    the details of a question identified by its ID.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            question = get_by_id(id)
            question.delete()
            return Response(
                {"status": "True", "message": "Question Deleted Successfully"}
            )
        except QuestionRepository.DoesNotExist:
            return Response(
                {"status": "False", "message": "Id Doesn't exists!!"},
                status=status.HTTP_404_NOT_FOUND,
            )
