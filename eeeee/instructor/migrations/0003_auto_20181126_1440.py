# Generated by Django 2.1.3 on 2018-11-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_auto_20181126_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='negative_marks',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='question',
            name='positive_marks',
            field=models.IntegerField(default=3),
        ),
    ]
