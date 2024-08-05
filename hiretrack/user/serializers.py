# myapp/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from phonenumber_field.serializerfields import PhoneNumberField

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
