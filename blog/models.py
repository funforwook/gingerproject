from django.db import models
from django.utils import timezone

# Create your models here.
class Favorite(models.Model):
    contents = models.URLField(max_length=200, null=True
    )
    created_at  = models.DateTimeField('작성시간', default=timezone.now)

class Save(models.Model):
    created_at = models.DateTimeField('작성시간', default=timezone.now)
