from django.db import models

# Create your models here.


class Status(models.Model):
    title = models.CharField(max_length=64,verbose_name="Назва")
    it_end = models.BooleanField(verbose_name="Це закрита угода?")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Статус заявки"
        verbose_name_plural = "Статуси заявок"


class RequestDocument(models.Model):
    title = models.CharField(max_length=256, verbose_name="Назва Заявки")
    document = models.FileField(null=True, blank=True, verbose_name="Файл документу")
    price = models.FloatField(verbose_name="Ціна [UAH]")
    date_conclusion = models.DateField(verbose_name="Дата складання договору", blank=True, null=True)
    date_payment = models.DateField(verbose_name="Дата оплати", blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Створено")

    def __str__(self) -> str:
        return f"#{self.id} {self.title}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заяви"


class RequestEvent(models.Model):
    document = models.ForeignKey(RequestDocument, on_delete=models.CASCADE, verbose_name="Заявка", related_name="event")
    author = models.CharField(max_length=256, verbose_name="Автор")
    title = models.CharField(max_length=256, verbose_name="Назва події")
    detail = models.TextField(verbose_name="Опис події")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Створено")
    old_status = models.ForeignKey(Status, null=True, verbose_name="Статус до зміни", on_delete=models.SET_NULL,
                                   related_name="old_status")
    new_status = models.ForeignKey(Status, null=True, verbose_name="Статус після зміни", on_delete=models.SET_NULL,
                                   related_name="new_status")

    def __str__(self) -> str:
        return f"#{self.document.id} {self.document.title} {self.title}"

    class Meta:
        verbose_name = "Подія завявки"
        verbose_name_plural = "Події заявок"
