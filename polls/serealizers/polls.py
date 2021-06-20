from rest_framework import serializers
from polls.models import Poll, Question, Choices, Answer


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'poll', 'text', 'type', 'choices']


class PollSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Poll
        read_only_fields = ['start_date']
        fields = ['id', 'title', 'start_date', 'end_date', 'description']


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'start_date', 'end_date', 'description', 'questions']

    def create(self, validated_data):
        poll = Poll.objects.create(**validated_data)
        return poll


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'user_id', 'poll', 'question', 'choices', 'text']


class AnswerUserSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True)
    question = QuestionSerializer()
    poll = PollSerializer()
    class Meta:
        model = Answer
        fields = ['id', 'user_id', 'poll', 'question', 'choices', 'text']
