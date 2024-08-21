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
    TeamMembersSerializer,
)
from .models import Team
from Teams.query import get_by_id, get_team_members, get_member_id, get_all_user
from rest_framework.permissions import IsAuthenticated


class CreateTeamView(APIView):
    def post(self, request):
        try:
            serializer = CreateTeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Team created successfully", "team": serializer.data},
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))


class GetTeamView(APIView):
    def get(self, request, id):
        try:
            team = get_by_id(id)
            serializer = CreateTeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Team.DoesNotExist:
            raise NotFound("Message : Team not found")

        except Exception as e:
            raise APIException(detail=str(e))


class DeleteTeamView(APIView):
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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        team_members = get_team_members()
        serializer = TeamMembersSerializer(team_members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamMembersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamMembersDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        team_members = get_member_id(id)
        team_members.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateTeamView(APIView):
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
