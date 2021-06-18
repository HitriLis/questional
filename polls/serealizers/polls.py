from rest_framework import serializers
from polls.models import Poll, Question, Choices


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'choices']


class QuestionSerializerCreate(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'poll', 'text', 'type', 'choices']

    def create(self, validated_data):
        print(validated_data)
        if validated_data['type'] == 'text':
            question = Question.objects.create(**validated_data)
        else:
            if 'choices' not in validated_data:
                raise serializers.ValidationError({"choices": ["Обязательное поле."]})
            else:
                question = Question.objects.create(**validated_data)
                choices = validated_data['choices']
                ChoicesSerializer(question=question, data=choices)
                print('klkl')
        return question


class PollSerializerUpdate(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'end_date', 'description', 'questions']


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'start_date', 'end_date', 'description', 'questions']

    def create(self, validated_data):
        poll = Poll.objects.create(**validated_data)
        return poll
