from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
  title=models.CharField(max_length=255)
  summary=models.TextField(null=True)
  content=models.TextField()
  created_at=models.DateTimeField(default=timezone.now)
  published_at=models.DateTimeField(null=True)
  is_published=models.BooleanField(default=False)