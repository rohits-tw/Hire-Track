from django.urls import path
from .views import MyModelListCreate, MyModelDetail

urlpatterns = [
    path('mymodels/', MyModelListCreate.as_view(), name='mymodel-list-create'),
    path('mymodels/<int:pk>/', MyModelDetail.as_view(), name='mymodel-detail'),
]
