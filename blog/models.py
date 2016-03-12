from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class posts(models.Model):
    title= models.CharField(max_length=200, null=True)
    text=models.TextField(null=True)
    author= models.ForeignKey('auth.User')
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(
                                        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
