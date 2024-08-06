from rest_framework import serializers
from .models import CustomUser, UserDetail

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'is_active', 'is_staff']

class UserDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = UserDetail
        fields = [
            'id', 'user', 'firstname', 'lastname', 'fullname', 
            'role', 'gender', 'profile_picture', 'address', 
            'created_at', 'updated_at', 'created_by', 'updated_by'
        ]

    def get_user(self, obj):
        """Return a nested representation of the related CustomUser."""
        return CustomUserSerializer(obj.user).data
