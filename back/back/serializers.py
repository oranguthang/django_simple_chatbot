from django.contrib.auth.models import User, Group
from rest_framework import serializers
from questionnaire.models import QuestionnaireImport, Questionnaire


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('id', 'start_question_id', 'name')


class QuestionnaireImportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionnaireImport
        fields = ('url', 'status', 'json_file')
