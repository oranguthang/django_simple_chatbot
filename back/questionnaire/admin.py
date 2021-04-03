from django.contrib import admin
from .models import Questionnaire, QuestionAnswer, HistoryQuestionAnswer, QuestionAnswerRelation, QuestionnaireImport

admin.site.register(Questionnaire)
admin.site.register(QuestionAnswer)
admin.site.register(HistoryQuestionAnswer)
admin.site.register(QuestionAnswerRelation)
admin.site.register(QuestionnaireImport)
