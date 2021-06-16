from django.db import models


class Interview(models.Model):
    title = models.CharField("Название", max_length=255)
    start_date = models.DateTimeField("Дата старта", blank=True, null=True)
    end_date = models.DateTimeField("Дата окончания", blank=True, null=True)
    description = models.DateTimeField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.title

