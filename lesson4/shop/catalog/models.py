from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name='Название')
    delivery_date = models.DateField(verbose_name='Дата поставки')
    price = models.PositiveIntegerField(verbose_name='Цена')
    measurement = models.CharField(max_length=5, blank=False, verbose_name='Единица измерения')
    provider = models.CharField(max_length=50, verbose_name='Поставщик')

    def __str__(self):
        return self.name
