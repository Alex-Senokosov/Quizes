from django.db import models
from django.contrib.auth.models import User
class Myquize (models.Model):
    title = models.CharField(max_length=255)  # Название квиза (тема - дублирование по каждому вопросу)
    question = models.TextField(blank=True)  # Вопрос
    answer_1 = models.TextField(blank=True)  # ответ 1
    answer_2 = models.TextField(blank=True)  # ответ 2
    answer_3 = models.TextField(blank=True)  # ответ 3
    answer_correct = models.TextField(blank=True)  # ответ правильный
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)  # кто добавил запись
    def __str__(self) :
        return self. title


class Category (models. Model):
    name = models. CharField (max_length=100, db_index=True)
    def __str__(self):
        return self .name
