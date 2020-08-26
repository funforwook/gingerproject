from django.db import models
from django.utils import timezone
from django.conf import settings #유저모델

# Create your models here.
class Favorite(models.Model):
    contents = models.URLField(max_length=200, null=True
    )
    created_at  = models.DateTimeField('작성시간', default=timezone.now)

class Save(models.Model):
    created_at = models.DateTimeField('작성시간', default=timezone.now)

class Add(models.Model):
    objects = models.Manager()
    link = models.URLField('링크')
    tag = models.CharField('태그',max_length=200,null=True)
    comments = models.CharField("코멘트", max_length=200,null=True)

    def __str__(self):
        return self.link