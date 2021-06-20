from django.db import models


class Poll(models.Model):
    title = models.CharField("Название", max_length=150)
    start_date = models.DateField("Дата старта")
    end_date = models.DateField("Дата окончания")
    description = models.TextField("Описание", max_length=500)

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name="questions", verbose_name="Опрос", on_delete=models.PROTECT)
    CHOICES = (
        ('text', 'Ответ текстом'),
        ('radio', 'Ответ с выбором одного варианта'),
        ('checkbox', 'Ответ с выбором нескольких вариантов')
    )
    text = models.TextField("Текст вопроса", max_length=500)
    type = models.CharField("Тип вопроса", max_length=300, choices=CHOICES)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choices(models.Model):
    title = models.CharField("Название", max_length=150)
    question = models.ForeignKey(Question, related_name="choices", verbose_name="Опрос", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Answer(models.Model):
    poll = models.ForeignKey(Poll, verbose_name="Опрос", on_delete=models.PROTECT)
    choices = models.ManyToManyField(Choices, verbose_name="Вариант", blank=True)
    question = models.ForeignKey(Question,  related_name="answer", verbose_name="Вопрос", on_delete=models.PROTECT)
    user_id = models.IntegerField("Id пользователя")
    text = models.CharField("Текст ответа", max_length=250, blank=True, null=True)

