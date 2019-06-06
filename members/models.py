from django.db import models

# Create your models here.


class Part(models.Model):
    name = models.CharField(max_length=10)
    short = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.name}'


class MudanNo(models.Model):
    num = models.IntegerField()

    def __str__(self):
        return f'{self.num}'


class UniveNo(models.Model):
    num = models.IntegerField()

    def __str__(self):
            return f'{self.num}'


class Major(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title}'


class Alive(models.Model):
    content = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.content}'


class Member(models.Model):
    name = models.CharField(max_length=10)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    mudanNo = models.ForeignKey(MudanNo, on_delete=models.CASCADE)
    univNo = models.ForeignKey(UniveNo, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    alive = models.ForeignKey(Alive, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mudanNo}_{self.part}_{self.name}'

    class Meta:
        ordering = ['mudanNo', 'part_id']

