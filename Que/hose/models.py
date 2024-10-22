from django.db import models


class Dolznosti(models.Model):
    dol = models.CharField('Должность', max_length=50, default='Что-то сломалось')

    def __str__(self):
        return self.dol

    class Meta:
        verbose_name = 'Должности'
        verbose_name_plural = 'А1. Должности'


class Sotrudniki(models.Model):
    fio = models.CharField('ФИО', max_length=150, default='Что-то сломалось')
    dol = models.ForeignKey(Dolznosti, on_delete=models.PROTECT)
    uda = models.CharField('Увольнение', max_length=1, default='Что-то сломалось')
    # Не int, т.к. предпочитаю единообразие
    dat = models.CharField('Дата увольнения', max_length=11, default='Что-то сломалось')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Б1. Сотрудники (А1)'
