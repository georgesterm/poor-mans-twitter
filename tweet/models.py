from django.db import models
from django.utils import timezone

# Create your models here.
class Messages(models.Model):
  writter = models.CharField(max_length=60, null=False)
  message = models.CharField(max_length=255, null=False)
  created_at = models.DateTimeField(default=timezone.now())

  def save(self, *args, **kwargs):
    if not self.id:
      self.created_at = timezone.now()
    return super().save(*args, **kwargs)