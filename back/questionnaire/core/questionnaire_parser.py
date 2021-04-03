from questionnaire.models import QuestionAnswer, QuestionAnswerRelation, Questionnaire


class QuestionnaireParser:
    """
    Class for validating and saving questionnaires given in JSON dictionary
    """
    def __init__(self, questionnaire):
        self.name = questionnaire['name']
        self.tree = questionnaire['tree']

    def __save_node(self, tree):
        is_leaf = False if 'response' in tree else True
        question_from = QuestionAnswer.objects.create(name=tree['text'], is_leaf=is_leaf)

        if not is_leaf:
            for response in tree['response']:
                QuestionAnswerRelation.objects.create(condition=response, question_from_id=question_from,
                                                      question_to_id=self.__save_node(tree['response'][response]))

        return question_from

    def __check_responses_count(self, tree):
        question = ""
        if 'response' in tree:
            if len(tree['response']) > 5:
                question = tree['text']
            else:
                for response in tree['response']:
                    question = self.__check_responses_count(tree['response'][response])
                    if question:
                        break
        return question

    def validate(self):
        questionnaire_exists = Questionnaire.objects.filter(name=self.name).count()
        is_valid = True
        message = ""

        if questionnaire_exists:
            is_valid = False
            message = ("Cannot save the questionnaire '{name}', because "
                       "the questionnaire with the same name already exists").format(name=self.name)

        unallowable_question = self.__check_responses_count(self.tree)
        if unallowable_question:
            is_valid = False
            message = ("Cannot save the questionnaire '{name}', because "
                       "the question '{question}' has more than 5 answers").format(name=self.name,
                                                                                   question=unallowable_question)

        return is_valid, message

    def save(self):
        Questionnaire.objects.create(name=self.name, start_question_id=self.__save_node(self.tree))
