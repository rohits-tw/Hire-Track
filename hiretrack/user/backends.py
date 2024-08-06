# myapp/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, phone_number=None, password=None, **kwargs):
        if email:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return None
        elif username:
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                return None
        elif phone_number:
            try:
                user = CustomUser.objects.get(phone_number=phone_number)
            except CustomUser.DoesNotExist:
                return None
        else:
            return None

        if user.check_password(password):
            return user
        return None
