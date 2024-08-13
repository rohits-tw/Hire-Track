from django.urls import path
from Teams.views import CreateTeam,GetTeam,DelTeam,TeamMembersListCreateView,TeamMembersDeleteView


urlpatterns = [
   
    path('create-team/', CreateTeam.as_view(), name='create-team'),
    path('get-team/<int:id>/', GetTeam.as_view(), name='get-team'),
    path('delete-team/<int:id>/', DelTeam.as_view(), name='del-team'),
    path('team-members/', TeamMembersListCreateView.as_view(), name='team-members-list-create'),
    path('delete-team-member/<int:id>/', TeamMembersDeleteView.as_view(), name='team-members--delete'),




]



