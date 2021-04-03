from django.contrib.auth.models import User, Group
from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework import status

from questionnaire.models import QuestionnaireImport, QuestionAnswer, QuestionAnswerRelation, Questionnaire, \
    HistoryQuestionAnswer
from back.serializers import UserSerializer, GroupSerializer, QuestionnaireImportSerializer, \
    QuestionnaireSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class QuestionnaireViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class QuestionnaireImportViewSet(viewsets.ModelViewSet):
    """
    API endpoint for importing questionnaires from JSON files.
    """
    queryset = QuestionnaireImport.objects.all()
    serializer_class = QuestionnaireImportSerializer


class QuestionWithAnswers(views.APIView):
    """
    APIView for getting question with possible answers by id of current question.
    """
    def get(self, request):
        question_id = request.GET.get('id', None)
        question = QuestionAnswer.objects.get(id=question_id)
        relations = QuestionAnswerRelation.objects.filter(question_from_id=question_id)

        if len(relations):
            result = question.name + ' (' + '/'.join(rel.condition for rel in relations) + ')'
        else:
            result = question.name

        response = Response({'text': result}, status=status.HTTP_200_OK)
        return response


class NextQuestion(views.APIView):
    """
    APIView for getting next question by current question id and user's answer.
    """
    def get(self, request):
        question_id = request.GET.get('id', None)
        answer = request.GET.get('answer', None)
        if answer:
            answer = answer.strip().lower()
        uuid = request.GET.get('uuid', None)
        next_question = QuestionAnswerRelation.objects.filter(question_from_id=question_id, condition__iexact=answer)

        if next_question:
            next_question = next_question[0]
            relations = QuestionAnswerRelation.objects.filter(question_from_id=next_question.question_to_id.id)
            result = {
                'id': next_question.question_to_id.id,
                'name': next_question.question_to_id.name,
            }
            if len(relations):
                result['name'] += ' (' + '/'.join(rel.condition for rel in relations) + ')'

            HistoryQuestionAnswer.objects.create(question_id=QuestionAnswer.objects.get(id=question_id),
                                                 answer=answer, uuid=uuid)
            if next_question.question_to_id.is_leaf:
                answers_history = HistoryQuestionAnswer.objects.filter(uuid=uuid).order_by('date_create')
                str_history = "Answers history: " + answers_history[0].question_id.name + ": "
                str_history += ' -> '.join([ans.answer for ans in answers_history])
                print(str_history)
        else:
            result = {
                'id': None,
                'name': None,
            }

        response = Response(result, status=status.HTTP_200_OK)
        return response
