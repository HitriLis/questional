from polls.serealizers.polls import (PollSerializer, PollSerializerUpdate, QuestionSerializer,
                                     ChoicesSerializer, AnswerSerializer, AnswerUserSerializer)
from polls.models import Poll, Question, Choices, Answer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from datetime import date


class PollsView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'update':
            return PollSerializerUpdate
        return PollSerializer

    def get_queryset(self):
        return Poll.objects.all()


class PollsViewList(viewsets.ReadOnlyModelViewSet):
    serializer_class = PollSerializer

    def get_queryset(self):
        today = date.today()
        return Poll.objects.filter(end_date__gte=today, start_date=today)


class QuestionsViewList(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()


class ChoicesView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = ChoicesSerializer

    def get_queryset(self):
        return Choices.objects.all()


class AnswerView(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.all()


class AnswerUserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = AnswerUserSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        filter_value = self.request.query_params.get('user_id', None)
        if filter_value is not None:
            queryset = queryset.filter(user_id=filter_value)
        return queryset
