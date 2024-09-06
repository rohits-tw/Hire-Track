from mom.models import Mom
from interview.models import InterviewForUser


def get_mom_by_interview_id(interview_id):
    mom = Mom.objects.filter(interview_id=interview_id)
    return mom


def get_all_mom():
    mom = Mom.objects.all()
    return mom


def get_by_id(id):
    team = Mom.objects.get(id=id)
    return team


def update_by_interview_id(interview_id):
    mom = Mom.objects.get(interview_id=interview_id)
    return mom
