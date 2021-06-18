from rest_framework.decorators import action
from polls.serealizers.polls import (PollSerializer, PollSerializerUpdate, QuestionSerializer, QuestionSerializerCreate,
                                     ChoicesSerializer)
from polls.models import Poll, Question, Choices
from rest_framework import viewsets, filters
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

    @action(detail=True, methods=['POST'])
    def add_question(self, request, pk=None):
        print(request)


class PollsViewList(viewsets.ReadOnlyModelViewSet):
    serializer_class = PollSerializer

    def get_queryset(self):
        today = date.today()
        return Poll.objects.filter(end_date__gte=today)


class QuestionsViewList(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionSerializer
        return QuestionSerializerCreate

    def get_queryset(self):
        return Question.objects.all()


class ChoicesView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = ChoicesSerializer

    def get_queryset(self):
        return Choices.objects.all()
