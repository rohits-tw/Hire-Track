from Teams.models import Team

def get_by_id(team_id):
    team = Team.objects.get(id=team_id)
    return team