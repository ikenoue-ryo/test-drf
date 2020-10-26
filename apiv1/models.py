from django.db import models
from datetime import datetime


class Writer(models.Model):
    name = models.CharField(max_length=128)

class Article(models.Model):
    writer = models.ForeignKey(Writer, related_name='articles',  on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    contents = models.TextField()
