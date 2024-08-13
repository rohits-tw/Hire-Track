from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException
from .serializers import CreateTeamSerializer
from Teams.query import get_by_id,get_team_members,get_member_id
from rest_framework.permissions import IsAuthenticated


class CreateTeam(APIView):
    def post(self, request):
        try:
            new_data = CreateTeamSerializer(data=request.data)
            if new_data.is_valid():
                team = new_data.save()
                return Response({"message": "Team created successfully", "team":team.new_data}, status=status.HTTP_201_CREATED)
            
            raise ValidationError(serializer.errors)
        
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            raise APIException(detail=str(e))



class GetTeam(APIView):
    def get(self, request, team_id):
        try:
            team = get_by_id(team_id)
            serializer = CreateTeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Team.DoesNotExist:
            raise NotFound(detail="Team not found",status = status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            raise APIException(detail=str(e))


class DelTeam(APIView):
    def delete(self, request, team_id):
        try:
            team =get_by_id(team_id)
            
            team.delete()
            
            return Response({"detail": "Team deleted successfully"}, status=status.HTTP_200_OK)
        
        except Team.DoesNotExist:
            raise NotFound(detail="Team not found", status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            raise APIException(detail=str(e))


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
            team_member = serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TeamMembersDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        team_member = get_member_id(id)
        team_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


