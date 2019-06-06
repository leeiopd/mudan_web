from django.db import models
from members.models import Member

# Create your models here.


class Year(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Concert(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.name}'

class Team(models.Model):
    name = models.CharField(max_length=30)
    team_members = models.ManyToManyField(Member, related_name='member_videoteam', blank=True)

    def __str__(self):
        return f'{self.name}'


class Video(models.Model):
    song_title = models.TextField()
    song_band = models.CharField(max_length=30)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    url = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.song_title}'




