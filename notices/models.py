from django.db import models

# Create your models here.


class Onenotice(models.Model):
    content = models.CharField(max_length=20)


class Notice(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    content = models.TextField()
