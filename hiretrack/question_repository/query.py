from question_repository.models import QuestionRepository


def get_question_by_team_id(id):
    Questions= QuestionRepository.objects.filter(team=id).all()
    return Questions


def get_by_id(id):
    Question = QuestionRepository.objects.get(id=id)
    return Question