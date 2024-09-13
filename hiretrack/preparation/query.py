from preparation.models import PreparationModel, BookMarkModel
from user.models import CustomUser


def get_all_material():
    preparation = PreparationModel.objects.all()
    return preparation


def get_by_id(id):
    preparation = PreparationModel.objects.get(id=id)
    return preparation


def get_bookmark_id(id):
    return BookMarkModel.objects.get(id=id)


def get_BookMark_By_UserId(user_id):
    Bookmark = BookMarkModel.objects.select_related("material").filter(user_id=user_id)
    return Bookmark
