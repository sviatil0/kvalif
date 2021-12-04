from django.db import models

# Create your models here.

class ESP(models.Model):
    name = models.TextField(max_length=20)
    mode = models.BooleanField(default=True)
    password = models.TextField()