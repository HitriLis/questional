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
    question = models.ForeignKey(Question, related_name="choices", verbose_name="Poll", on_delete=models.PROTECT)


class Answer(models.Model):
    choices = models.ForeignKey(Choices, verbose_name="Poll", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name="Poll", on_delete=models.CASCADE)


class User(models.Model):
    user_id = models.CharField("Номер заказа", max_length=255, unique=True)
