from .models import CustomUser


def get_all_user():
    user = CustomUser.objects.select_related("user_detail").all()
    return user


def get_user(id):
    user_objs = CustomUser.objects.select_related("user_detail").filter(id=id)
    return user_objs
