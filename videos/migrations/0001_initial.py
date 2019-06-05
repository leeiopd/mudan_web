# Generated by Django 2.1.8 on 2019-06-05 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('team_members', models.ManyToManyField(blank=True, related_name='member_videoteam', to='members.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.TextField()),
                ('song_band', models.CharField(max_length=10)),
                ('url', models.TextField()),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Concert')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Year'),
        ),
    ]
