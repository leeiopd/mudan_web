# Generated by Django 2.1.8 on 2019-06-05 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowsong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('band', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Nowteam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('short_name', models.CharField(max_length=1)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worktimes.Color')),
                ('members', models.ManyToManyField(blank=True, related_name='member_nowteam', to='members.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Workhour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workweek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='table',
            name='hour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worktimes.Workhour'),
        ),
        migrations.AddField(
            model_name='table',
            name='nowteam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worktimes.Nowteam'),
        ),
        migrations.AddField(
            model_name='table',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worktimes.Workweek'),
        ),
        migrations.AddField(
            model_name='nowsong',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worktimes.Nowteam'),
        ),
    ]
