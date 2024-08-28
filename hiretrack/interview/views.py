from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from interview.serializers import (
    CreateInterviewSerializer,
    ListInterviewSerializer,
    UpdateStatusSerializer,
    ListAllInterviewSerializer,
    ListInterviewHistoryByUserIdSerializer,
)
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.permissions import IsAuthenticated
from interview.models import InterviewForUser
from interview.query import (
    get_interview_details_by_id,
    get_all_interview_details,
    get_interview_from_user_id,
    get_by_id,
)


# Create your views here.
class CreateInterviewsView(APIView):
    """
    View to handle create unterview for the currently authenticated user:
    This view handles POST requests to create interview for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = CreateInterviewSerializer(data=request.data)
            if serializer.is_valid():
                interview = serializer.save()
                return Response(
                    {
                        "message": "Interview scheduled successfully",
                        "interview id": str(interview.id),
                    },
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))


class ListInterviewsView(APIView):
    """
    View to handle list interview by id for the currently authenticated user:
    This view handles GET requests to get interview for the logged-in user.
    It checks if interview details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            interview_by_id = get_interview_details_by_id(id)
            serializer = ListInterviewSerializer(interview_by_id)
            return Response(
                {"status": True, "message": "Interview", "Interview": serializer.data}
            )
        except InterviewForUser.DoesNotExist:
            return Response(
                {"status": False, "message": "Interview ID not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class ListAllInterviewsView(APIView):
    """
    View to handle list all interview for the currently authenticated user:
    This view handles GET requests to get all interview for the logged-in user.
    It checks if interview details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            all_interview = get_all_interview_details()
            serializer = ListAllInterviewSerializer(all_interview, many=True)
            return Response(
                {
                    "status": True,
                    "message": "All interview",
                    "All-Interviews": serializer.data,
                }
            )
        except InterviewForUser.DoesNotExist:
            return Response(
                {"status": False, "message": "Interview Details not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class ListInterviewHistoryByUserId(APIView):
    """
    View to handle list all interview according to the interviewer id for the currently authenticated user:
    This view handles GET requests to get all interview according to the interviewer id for the logged-in user.
    It checks if interview details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        interviews = get_interview_from_user_id(id)
        if not interviews.exists():
            return Response(
                {"status": False, "message": "No interviews found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class UpdateInterviewStatusView(APIView):
    """
    View to handle update interview stauts by id for the currently authenticated user:
    This view handles POST requests to update interview status for the logged-in user.
    It checks if interview details are not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UpdateStatusSerializer

    def post(self, request, id):
        try:
            interview = get_by_id(id)
        except InterviewForUser.DoesNotExist:
            return Response(
                {"status": False, "message": "interview id not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(interview, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "interview status updated successfully"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = ListInterviewHistoryByUserIdSerializer(interviews, many=True)
        return Response(
            {"status": True, "message": "Interview", "interviews": serializer.data}
        )