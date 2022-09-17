from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField(max_length=300)
