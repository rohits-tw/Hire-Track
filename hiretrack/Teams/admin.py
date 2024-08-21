from django.contrib import admin
from Teams.models import Team,TeamMembers

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name','team_lead','created_by','created_at','updated_by','updated_at')
    search_fields = ('name', 'team_lead')



@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('id','member','designation','allotment_date','active')
    search_fields = ('member', 'active')


