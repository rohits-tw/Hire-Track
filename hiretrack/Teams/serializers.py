from rest_framework import serializers
from Teams.models import Team, TeamMembers


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


class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = [
            "id",
            "allotment_team",
            "member",
            "designation",
            "allotment_date",
            "active",
        ]

    def save(self, **kwargs):
        allotment_team = self.validated_data.get("allotment_team")
        member = self.validated_data.get("member")
        designation = self.validated_data.get("designation")
        active = self.validated_data.get("active", True)

        if not allotment_team or not member:
            raise serializers.ValidationError(
                "Allotment team and member are required fields."
            )

        instance = TeamMembers(
            allotment_team=allotment_team,
            member=member,
            designation=designation,
            active=active,
        )
        instance.save()

        return instance


class UpdateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "description"]


class GetAllTeamserializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "description", "team_lead"]


class GetTeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ["id", "designation", "allotment_date", "active"]
