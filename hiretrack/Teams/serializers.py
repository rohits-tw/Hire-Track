from rest_framework import serializers
from Teams.models import Team


class CreateTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"

    def create(self, validated_data):
        """
        Creating and returning a new team instance.
        """
        team = Team.objects.create(
            name=validated_data["name"],
            description=validated_data.get("description", ""),
            team_lead=validated_data["team_lead"],
        )

        team.save()
        return team


class UpdateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "description"]


class GetAllTeamserializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "description", "team_lead"]
