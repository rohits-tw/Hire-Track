from rest_framework import serializers
from .models import CustomUser, UserDetail
from django.contrib.auth import authenticate
from phonenumber_field.serializerfields import PhoneNumberField
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email')
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


from phonenumber_field.serializerfields import PhoneNumberField # type: ignore


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    phone_number = PhoneNumberField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        phone_number = data.get('phone_number')
        password = data.get('password')

        if not email and not username and not phone_number:
            raise serializers.ValidationError('Email, username or phone number is required to login.')

        user = None
        if email:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
        elif username:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
        elif phone_number:
            user = authenticate(request=self.context.get('request'), phone_number=phone_number, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        data['user'] = user
        return data


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

