from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False,
                             verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    date_posted = models.DateTimeField(default=timezone.now,
                                       verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор')

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
