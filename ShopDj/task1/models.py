from django.db import models

# Create your models here.

# В этом домашнем задании Вам нужно будет добавить новую вкладку с пагинацией в главном меню.
# Для этого Вам понадобится
# Создать модель News с полями title, content, date.



class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Buyer(models.Model):
    name = models.CharField(max_length=15)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=15)
    cost = models.DecimalField(max_digits=6,decimal_places=2)
    size = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField(blank=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

