from operator import mod
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """사용자가 배우고 있는 주제"""
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """모델을 문자열로 반환합니다"""
        return self.text

class Entry(models.Model):
    """주제에 관해 배운 것"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """모델을 문자열로 반환합니다"""
        return f"{self.text[:50]}..."        