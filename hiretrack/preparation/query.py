from preparation.models import PreparationModel
from user.models import CustomUser


def get_all_material():
    preparation = PreparationModel.objects.all()
    return preparation


def get_by_id(id):
    preparation = PreparationModel.objects.get(id=id)
    return preparation
