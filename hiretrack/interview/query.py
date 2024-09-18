from interview.models import InterviewForUser


def get_interview_details_by_id(id):
    interview = InterviewForUser.objects.get(id=id)
    return interview


def get_all_interview_details():
    interviews = InterviewForUser.objects.all()
    return interviews


def get_interview_from_user_id(id):
    interview = InterviewForUser.objects.filter(interviewer_id=id).all()
    return interview


def get_by_id(id):
    interview = InterviewForUser.objects.get(id=id)
    return interview 