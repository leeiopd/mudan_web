# Generated by Django 2.1.8 on 2019-06-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktimes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nowsong',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='nowteam',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
