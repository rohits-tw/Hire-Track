from django.contrib import admin
from Teams.models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name','team_lead','created_by','created_at','updated_by','updated_at')
    search_fields = ('name', 'team_lead')


