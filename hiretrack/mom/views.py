from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.permissions import IsAuthenticated
from mom.serializers import (
    MomSerializer,
    UpdateMomSerializer,
    GetAllMomSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from mom.query import (
    get_mom_by_interview_id,
    get_all_mom,
    get_by_id,
    update_by_interview_id,
)
from mom.models import Mom
from django.db.models import Q
from rest_framework import generics


class CreateMomView(APIView):
    """
    View to handle create Minutes of meeting:
    This view handles POST requests to create Minutes of meeting repository.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = MomSerializer(data=request.data)
            if serializer.is_valid():
                Mom = serializer.save()
                return Response(
                    {
                        "Mom_id": str(Mom.id),
                        "message": "MOM added successfully",
                    },
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))


class GetMomByInterviewIdView(APIView):
    """
    API view to list mom for a specific Interview ID for the authenticated user.

    Handles GET requests to retrieve mom associated with a given Interview ID.
    Returns an error message if no mom is found.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        mom = get_mom_by_interview_id(id)
        if not mom.exists():
            return Response(
                {"status": False, "message": "No mom Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MomSerializer(mom, many=True)
        return Response({"status": True, "Questions": serializer.data})


class UpdateMomByInterviewIdView(APIView):
    """
    API view to update the Mom record for a specific Interview ID.
    Handles PUT requests to update mom details associated with a given Interview ID.
    """

    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            mom = update_by_interview_id(id)
        except Mom.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "Mom not found for the given interview ID.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = UpdateMomSerializer(mom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Mom updated successfully",
                    "mom": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllMomView(APIView):
    """
    View to handle get all mom for the currently authenticated user:
    This view handles GET requests to get all mom for the logged-in user.
    """

    def get(self, request):
        mom = get_all_mom()
        if mom:
            serializer = GetAllMomSerializer(mom, many=True)
            return Response(
                {"status": True, "message": "All Mom", "Mom": serializer.data}
            )
        else:
            return Response(
                {"status": False, "message": "No Mom found"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class DeleteMomView(APIView):
    """
    View to handle delete mom by id for the currently authenticated user:
    This view handles DELETE requests to delete mom for the logged-in user.
    It checks if mom details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            mom = get_by_id(id)
            mom.delete()
            return Response(
                {"status": True, "message": "Mom deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except Mom.DoesNotExist:
            return Response(
                {"status": False, "message": "Mom not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class SearchMomAPIView(generics.ListAPIView):
    """
    API view to retrieve filtered MOM entries based on optional query parameters:
    - author_id: Filter by the user who created the MOM.
    - keyword: Search in the notes, keywords, or action items.
    - date_range: Filter by a date range (format: YYYY-MM-DD,YYYY-MM-DD).
    """

    serializer_class = GetAllMomSerializer

    def get_queryset(self):
        queryset = get_all_mom()
        try:
            author_id = self.request.query_params.get("author_id")
            if author_id:
                queryset = queryset.filter(author_id=author_id)
            keyword = self.request.query_params.get("keyword")
            if keyword:
                queryset = queryset.filter(
                    Q(notes__icontains=keyword) | Q(action_items__icontains=keyword)
                )
            start_date = self.request.query_params.get("start_date")
            end_date = self.request.query_params.get("end_date")
            if start_date and end_date:
                try:
                    queryset = queryset.filter(created_at__range=[start_date, end_date])
                except ValueError:
                    raise ValidationError(
                        "Invalid date format. Expected format is YYYY-MM-DD."
                    )
        except Exception as e:
            raise ValidationError(
                f"An error occurred while filtering MOM entries: {str(e)}"
            )
        return queryset
