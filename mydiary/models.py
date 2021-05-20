from django.db import models

# Create your models here.

class Content(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=100, blank=True, default='')
  text = models.TextField()

