# Generated by Django 2.1.8 on 2019-06-06 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20190607_0617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['part_id', 'mudanNo_id']},
        ),
    ]