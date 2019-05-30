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


class Nowsong(models.Model):
    title = models.CharField(max_length=10)
    band = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'


class Nowteam(models.Model):
    name = models.CharField(max_length=10)
    members = models.ManyToManyField(Member, related_name='member_nowteam', blank=True)
    days = models.ForeignKey(Workweek, on_delete=models.CASCADE)
    hours = models.ForeignKey(Workhour, on_delete=models.CASCADE)
    songs = models.ForeignKey(Nowsong, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.team}'
