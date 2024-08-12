from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException
from .serializers import CreateTeamSerializer
from Teams.query import get_by_id

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





