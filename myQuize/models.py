from django.db import models
from django.contrib.auth.models import User
class Myquize (models.Model):
    title = models.CharField (max_length=255) # Название квиза
    content = models.TextField(blank=True) # Содержание квиза
    cat = models.ForeignKey ('Category', on_delete=models.PROTECT, null=True) # категрии квизов
    user = models.ForeignKey (User, verbose_name="Пользователь", on_delete=models.CASCADE) # кто добавил запись


    def __str__(self) :
        return self. title


class Category (models. Model):
    name = models. CharField (max_length=100, db_index=True)
    def __str__(self):
        return self .name
