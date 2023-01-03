from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='Категория',
                            max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название')
    short_desc = models.CharField(
        max_length=255, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    # aviability = models.PositiveBigIntegerField(
    #     verbose_name='Остаток на складе')
    image = models.ImageField(upload_to='product_images', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
