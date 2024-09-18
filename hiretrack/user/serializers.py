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
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password", "confirm_password")

    def validate(self, attrs):
        """
        Validate that both password fields match.
        """
        if attrs["password"] != attrs["confirm_password"]:
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

    username = serializers.CharField(required=False)
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

        if username:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
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


class GetUserSerializers(serializers.ModelSerializer):
    user_detail = UserDetailSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "phone_number", "user_detail"]


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


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True, min_length=8)
    new_password = serializers.CharField(required=True, write_only=True, min_length=8)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # from .models import CustomUser

        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "No user is associated with this email address."
            )
        return value


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data
