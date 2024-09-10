from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from preparation.serializers import (
    AddPreparationSerializer,
    GetAllMaterialSerializer,
    AddBookMarkSerializer,

)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, APIException, NotFound
from rest_framework import status
from preparation.query import get_all_material, get_by_id
from preparation.models import PreparationModel
from django.db.models import Q


# Create your views here.
class AddPreparationView(APIView):
    """
    View to handle add preperation for the currently authenticated user:
    This view handles POST requests to add preperation for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = AddPreparationSerializer(data=request.data)
            if serializer.is_valid():
                interview = serializer.save()
                return Response(
                    {
                        "message": "Preparation material added successfully",
                        "material_id": str(interview.id),
                    },
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))


class GetAllMaterialView(APIView):
    """
    View to handle get all preperation material for the currently authenticated user:
    This view handles GET requests to get preperation for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            all_interview = get_all_material()
            serializer = GetAllMaterialSerializer(all_interview, many=True)
            return Response(
                {
                    "status": True,
                    "message": "All Material",
                    "All-Material": serializer.data,
                }
            )
        except PreparationModel.DoesNotExist:
            return Response(
                {"status": False, "message": "material Details not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class GetMaterialByIdView(APIView):
    """
    View to handle get preperation by material id for the currently authenticated user:
    This view handles GET requests to get preperation by material id for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            preperation = get_by_id(id)
            serializer = GetAllMaterialSerializer(preperation)
            return Response({"status": True, "material": serializer.data})

        except PreparationModel.DoesNotExist:
            raise NotFound("Message : Material not found")

        except Exception as e:
            raise APIException(detail=str(e))


class UpdateMaterialView(APIView):
    """
    View to handle update preperation by material id for the currently authenticated user:
    This view handles UPDATE requests to update preperation by material id for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        try:
            preperation = get_by_id(id)
            serializer = GetAllMaterialSerializer(
                preperation, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": True,
                        "material_id": str(preperation.id),
                        "message": "material updated successfully",
                    }
                )
        except PreparationModel.DoesNotExist:
            return Response(
                {"status": False, "message": "Material id not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteMaterialView(APIView):
    """
    View to handle delete preperation by material id for the currently authenticated user:
    This view handles DELETE requests to delete preperation by material id for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):

        prep_obj = PreparationModel.objects.filter(id=id).first()
        if prep_obj:
            prep_obj.delete()
            return Response(
                {
                    "status": True,
                    "message": "Preparation material deleted successfully",
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"status": False, "message": "Material not found"},
            status=status.HTTP_404_NOT_FOUND,
        )


class SearchMaterialView(APIView):
    """
    View to handle search preperation by type and tags for the currently authenticated user:
    This view handles SEARCH preperation by type and tags for the logged-in user.(It will run in postman query params)
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = get_all_material()
        type = request.query_params.get("type", None)
        if type:
            queryset = queryset.filter(Q(type__icontains=type))

        tags = request.query_params.get("tags", None)
        if tags:
            queryset = queryset.filter(Q(tags__icontains=tags))
        keyword = request.query_params.get("keyword", None)
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(content__icontains=keyword)
            )

        serializer = GetAllMaterialSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddBookMarkView(APIView):
    """
    View to handle add bookmark of material for the currently authenticated user:
    This view handles POST requests to add bookmark of material for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = AddBookMarkSerializer(data=request.data)
            if serializer.is_valid():
                interview = serializer.save()
                return Response(
                    {
                        "message": "Material bookmarked successfully",
                        "bookmark_id": str(interview.id),
                    },
                    status=status.HTTP_201_CREATED,
                )

            raise ValidationError(serializer.errors)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise APIException(detail=str(e))
