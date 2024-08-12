from django.urls import path
from Teams.views import test,CreateTeam,GetTeam


urlpatterns = [
   
    path('test/', test, name='test'),
    path('create-team/', CreateTeam.as_view(), name='create-team'),
    path('get-team/<int:id>/', GetTeam.as_view(), name='get-team'),


]



