from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException, NotFound
from .serializers import (
    CreateTeamSerializer,
    UpdateTeamSerializer,
    GetAllTeamserializer,
    GetTeamMembersSerializer,
    TeamMembersSerializer,
)
from .models import Team, TeamMembers
from Teams.query import (
    get_by_id,
    get_team_members,
    get_member_id,
    get_all_user,
    get_members,
)
from rest_framework.permissions import IsAuthenticated


class CreateTeamView(APIView):
    """
    View to handle create team for the currently authenticated user:
    This view handles POST requests to create team for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = CreateTeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Team created successfully", "Team": serializer.data},
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))


class GetTeamView(APIView):
    """
    View to handle get team by id for the currently authenticated user:
    This view handles GET requests to get team for the logged-in user.
    It checks if team details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            team = get_by_id(id)
            serializer = CreateTeamSerializer(team)
            return Response({"status": True, "Teams": serializer.data})

        except Team.DoesNotExist:
            raise NotFound("Message : Team not found")

        except Exception as e:
            raise APIException(detail=str(e))


class DeleteTeamView(APIView):
    """
    View to handle delete team by id efor the currently authenticated user:
    This view handles DELETE requests to delete team for the logged-in user.
    It checks if team details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            team = get_by_id(id)
            team.delete()
            return Response(
                {"status": True, "message": "Team deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except Team.DoesNotExist:
            return Response(
                {"status": False, "message": "Team not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


# List and Create Team Members
class TeamMembersListCreateView(APIView):
    """
    View to handle get team member by id for the currently authenticated user:
    This view handles GET requests to get team for the logged-in user.
    It checks if team member details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, team_id):
        try:
            team_members = get_members(team_id)
            serializer = GetTeamMembersSerializer(team_members, many=True)
            return Response(
                {"status": True, "message": "Team members", "Teams": serializer.data}
            )
        except TeamMembers.DoesNotExist:
            return Response(
                {"status": False, "message": "Team member not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    """
    View to handle create team member for the currently authenticated user:
    This view handles POST requests to create team for the logged-in user.
    It checks if team member details is not exists it returns an error.
    """

    def post(self, request):
        serializer = TeamMembersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "message": "Team Member added successfully"}
            )
        return Response({"status": False, "message": "Team Member not added!!"})


class TeamMembersDeleteView(APIView):
    """
    View to handle delete team member by id for the currently authenticated user:
    This view handles DELETE requests to delete team for the logged-in user.
    It checks if team member details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            team_members = get_member_id(id)
            team_members.delete()
            return Response(
                {"status": True, "message": "Team Member deleted successfully"}
            )
        except TeamMembers.DoesNotExist:
            return Response(
                {"status": False, "message": "Team member not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class UpdateTeamView(APIView):
    """
    View to handle update team by id for the currently authenticated user:
    This view handles POST requests to update team for the logged-in user.
    It checks if team details is not exists it returns an error.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UpdateTeamSerializer

    def post(self, request, id):
        try:
            team = get_by_id(id)
        except Team.DoesNotExist:
            return Response(
                {"status": False, "message": "Team id not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(team, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Team updated successfully"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllTeamView(APIView):
    """
    View to handle get all team for the currently authenticated user:
    This view handles GET requests to get all team for the logged-in user.
    """

    def get(self, request):
        team = get_all_user()
        if team:
            serializer = GetAllTeamserializer(team, many=True)
            return Response(
                {"status": True, "message": "Users fetched.", "Teams": serializer.data}
            )
        else:
            return Response(
                {"status": False, "message": "None Users"},
                status=status.HTTP_400_BAD_REQUEST,
            )
