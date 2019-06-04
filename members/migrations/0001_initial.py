# Generated by Django 2.1.8 on 2019-06-04 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('alive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Alive')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Major')),
            ],
        ),
        migrations.CreateModel(
            name='MudanNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('short', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='UniveNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='mudanNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.MudanNo'),
        ),
        migrations.AddField(
            model_name='member',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Part'),
        ),
        migrations.AddField(
            model_name='member',
            name='univNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.UniveNo'),
        ),
    ]
