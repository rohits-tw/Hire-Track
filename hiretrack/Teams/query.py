from Teams.models import Team, TeamMembers


def get_by_id(id):
    team = Team.objects.get(id=id)
    return team


def get_team_members():
    members = TeamMembers.objects.all()
    return members


def get_member_id(id):
    member = TeamMembers.objects.get(id=id)
    return member


def get_all_user():
    team = Team.objects.filter().all()
    return team


def get_members(team_id):
    members = TeamMembers.objects.filter(allotment_team=team_id).values()
    return members
