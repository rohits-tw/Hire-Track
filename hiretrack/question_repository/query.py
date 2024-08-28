from question_repository.models import QuestionRepository


def get_question_by_team_id(id):
    interview = QuestionRepository.objects.filter(team=id).all()
    return interview
