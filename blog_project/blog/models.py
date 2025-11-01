from django.db import models  # Импорт модуля models из Django

# Create your models here.  # Комментарий — указание, где создавать модели

class Post(models.Model):  # Объявление класса модели Post
    title = models.CharField(max_length=100)  # Поле «название» (до 100 символов)
    content = models.TextField()  # Поле «содержание» (текст без ограничения длины)
    author = models.CharField(max_length=100)  # Поле «автор» (до 100 символов)
    created_at = models.DateTimeField(auto_now_add=True)  (автоматически заполняется при создании записи)
