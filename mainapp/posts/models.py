from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    body = models.TextField(verbose_name='Описание')
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(verbose_name='Ваш комментарий', max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.сontent
