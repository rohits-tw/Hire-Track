from rest_framework import serializers
from .models import CustomUser, UserDetail
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.serializerfields import PhoneNumberField


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration. It includes email, password, and username fields.
    Validates the uniqueness of the email and ensures password confirmation.
    """

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "password", "password2", "email")

    def validate(self, attrs):
        """
        Validate that both password fields match.
        """
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.
        """
        user = CustomUser.objects.create(
            username=validated_data["username"], email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login. It includes email, username, or phone number fields along with the password.
    Validates that at least one of email, username, or phone number is provided.
    """

    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    phone_number = PhoneNumberField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Validate that at least one of email, username, or phone number is provided,
        and check the credentials for authentication.
        """
        email = data.get("email")
        username = data.get("username")
        phone_number = data.get("phone_number")
        password = data.get("password")

        if not email and not username and not phone_number:
            raise serializers.ValidationError(
                "Email, username, or phone number is required to login."
            )

        user = None
        if email:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )
        elif username:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
        elif phone_number:
            user = authenticate(
                request=self.context.get("request"),
                phone_number=phone_number,
                password=password,
            )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user
        return data


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "phone_number", "is_active", "is_staff"]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = [
            "id",
            "firstname",
            "lastname",
            "fullname",
            "role",
            "gender",
            "profile_picture",
            "address",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]

    # def get_user(self, obj):
    #     """Return a nested representation of the related CustomUser."""
    #     return CustomUserSerializer(obj.user).data


class GetUserSerializers(serializers.ModelSerializer):
    user_detail = UserDetailSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "phone_number", "user_detail"]


class AddUserDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = [
            "id",
            "firstname",
            "lastname",
            "fullname",
            "role",
            "gender",
            "profile_picture",
            "address",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = [
            "firstname",
            "lastname",
            "profile_picture",
            "address",
            "gender",
            "fullname",
        ]
