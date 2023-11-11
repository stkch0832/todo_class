from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string


def create_id():
    return get_random_string(10)


class Post(models.Model):
    STATUS_CHOICES = [
        (0, '未着手'),
        (1, '進行中'),
        (2, '一時中断'),
        (3, '中止'),
        (4, '完了'),
    ]

    id = models.CharField(
        default=create_id,
        primary_key=True,
        max_length=10,
        editable=False,
        )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    title = models.CharField(
        'タイトル',
        max_length=20,
        )
    status= models.IntegerField(
        'ステータス',
        choices=STATUS_CHOICES,
        )
    deadline = models.DateTimeField(
        '期限',
        )
    description = models.TextField(
        '詳細',
        max_length=255,
        )

    created_at = models.DateTimeField(
        '作成日時',
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        '更新日時',
        auto_now=True
        )

    def __str__(self):
        return self.title
