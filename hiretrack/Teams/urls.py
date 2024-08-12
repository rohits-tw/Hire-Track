from django.urls import path
from Teams.views import CreateTeam,GetTeam,DelTeam


urlpatterns = [
   
    path('create-team/', CreateTeam.as_view(), name='create-team'),
    path('get-team/<int:id>/', GetTeam.as_view(), name='get-team'),
    path('delete-team/', DelTeam.as_view(), name='del-team'),


]



