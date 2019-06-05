from django.db import models
from members.models import Member
# Create your models here.


class Workweek(models.Model):
    day = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.day}'


class Workhour(models.Model):
    clock = models.IntegerField()

    def __str__(self):
        return f'{self.clock}'

class Color(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Nowteam(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=1)
    members = models.ManyToManyField(Member, related_name='member_nowteam', blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Nowsong(models.Model):
    title = models.CharField(max_length=30)
    band = models.CharField(max_length=10)
    team = models.ForeignKey(Nowteam, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Table(models.Model):
    week = models.ForeignKey(Workweek, on_delete=models.CASCADE)
    hour = models.ForeignKey(Workhour, on_delete=models.CASCADE)
    nowteam = models.ForeignKey(Nowteam, on_delete=models.CASCADE)
