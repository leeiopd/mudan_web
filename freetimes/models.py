from django.db import models
from members.models import Member
# Create your models here.


class Freeweek(models.Model):
    day = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.day}'


class Freehour(models.Model):
    clock = models.IntegerField()

    def __str__(self):
        return f'{self.clock}'


class Table(models.Model):
    week = models.ForeignKey(Freeweek, on_delete=models.CASCADE)
    hour = models.ForeignKey(Freehour, on_delete=models.CASCADE)
    members = models.ManyToManyField(Member, related_name='member_freetimes', blank=True)

